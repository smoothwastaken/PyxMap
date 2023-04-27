# PyxMap
# Copyright © 2023 Cléry Arque-Ferradou, Nathanaël Lejuste, De Beaumont du Repaire Carla, Chasseigne Ulysse

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


# ---------------------------------------------------------------
# This feature is not yet implemented so this file is not used for now.
# But you can read it if you want to know how we planned to implement it.
# We tried to implement it but we have some issues due to the way the Firestore Database is working that weren't planned.
# We will try to implement it in the future and very soon.
# Sorry for the inconvenience.
# ---------------------------------------------------------------


import pygame
import numpy as np
import threading
from database import Database


class Map(object):

    def __init__(self) -> None:
        self.map = []

        if __name__ != "__main__":
            self.load_map()

    def load_map(self) -> None:
        # Load the map from the database
        # <-- Return a dictionary.
        self.all_pyxpics = Database().fetch_all_pyxpic()

    def display_map(self) -> None:
        matrices = (self.map_to_matrices(self.all_pyxpics))
        self.matrix_viewer(matrices)

    def get_raw_image(self, pyxpic: dict) -> str:
        result_matrix = []
        for key, value in pyxpic.items():
            if key == 'raw_image':
                for line_int, line_content in value.items():
                    temp_line = []
                    for e in line_content:
                        print(e, end="")
                        temp_line.append(e)
                    print("")
                    # print(temp_line)
                    result_matrix.append(temp_line)
                    # print(result_matrix)

                    # Remove empty lists from the map (bug fix from camera.py)
                    for e in result_matrix:
                        if len(e) == 0:
                            result_matrix.remove(e)

                result_matrix = np.array(
                    result_matrix)

        return result_matrix

    def map_to_matrices(self, map_data):
        matrices = []
        for pyxpic_id, pyxpic_data in map_data.items():
            print(pyxpic_id)
            matrix = self.get_raw_image(pyxpic_data)
            matrices.append(matrix)

        return matrices

    def draw_matrix(self, screen, font, matrices, zoom, offset_x, offset_y):
        cell_size = 0.5 * zoom
        num_matrices = len(matrices)
        square_size = int(np.ceil(np.sqrt(num_matrices)))
        matrix_width = matrices[0].shape[1] * cell_size

        for idx in range(square_size * square_size):
            row = idx // square_size
            col = idx % square_size

            x_offset = col * matrix_width
            y_offset = row * matrices[0].shape[0] * cell_size

            if idx < num_matrices:
                matrix = matrices[idx]

            for i in range(matrix.shape[0]):
                for j in range(matrix.shape[1]):
                    x = j * cell_size + offset_x + x_offset
                    y = i * cell_size + offset_y + y_offset
                    text = font.render(
                        str(matrix[i][j]), True, (255, 255, 255))
                    text_rect = text.get_rect(
                        center=(x + cell_size // 2, y + cell_size // 2))
                    screen.blit(text, text_rect)

    def matrix_viewer(self, matrices):
        pygame.init()
        screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption('Matrix Viewer')

        zoom_level = 25
        offset_x = 0
        offset_y = 0

        font = pygame.font.Font(None, 15)

        running = True
        while running:
            screen.fill((0, 0, 0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        offset_x += 20
                    elif event.key == pygame.K_RIGHT:
                        offset_x -= 20
                    elif event.key == pygame.K_UP:
                        offset_y += 20
                    elif event.key == pygame.K_DOWN:
                        offset_y -= 20
                    elif event.key == pygame.K_p or event.key == pygame.K_KP_PLUS:
                        zoom_level += 1
                    elif event.key == pygame.K_m or event.key == pygame.K_KP_MINUS:
                        zoom_level -= 1
                        if zoom_level < 1:
                            zoom_level = 1

            self.draw_matrix(screen, font, matrices,
                             zoom_level, offset_x, offset_y)

            pygame.display.flip()

        pygame.quit()


def main_thread():
    # while True:
    # Your main script tasks here
    pass


if __name__ == "__main__":
    my_map = Map()
    my_map.load_map()

    # Start the main_thread in a separate thread
    main_thread = threading.Thread(target=main_thread)
    main_thread.start()

    # Call display_map() in the main thread
    my_map.display_map()
