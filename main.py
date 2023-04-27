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


import json
from camera import Camera, CameraUtils
from database import Database, DatabaseUtils
from qrcode import QRCode
import time
import platform
import os


class App(object):

    # App variables
    config = {}

    # App states
    running = True
    speak = False

    # Initialisation of the app
    def __init__(self) -> None:
        """This function initializes the app.
        """
        # Load the config file
        self._load_config()

        # Detect the OS
        self.os = platform.system()

        # If MacOS, make the app speak !
        if self.os == "Darwin" and self.config['darwin_voice'] == True:
            self.speak = True

    def _load_config(self) -> None:
        """This function loads the config file.
        """
        # Load the config file
        with open("config.json", "r") as f:
            self.config = json.load(f)
            f.close()

    def run(self) -> None:
        """This function runs the app.
        """
        while self.running:

            if self.speak:
                os.system(
                    f'say "Salut ! Pour commencer, montre moi ta carte de cantine !"')

            # Instancing the QRCode class
            qr = QRCode()
            # Reading the QR Code
            owner_id = qr.read(camera=CameraUtils.list_cameras()[0])

            if self.speak:
                os.system(
                    """say "Merci, c'est parfait ! Maintenant, tu peux sourire !" """)

            time.sleep(1)
            # Instancing the Camera class
            cam = Camera(scale=5)
            # Capturing the frame
            capture = cam.capture()
            time.sleep(1)
            # Getting the normal frame
            normal_frame = cam.get_normal_frame(capture)
            # Getting the gray frame
            gray_frame = cam.get_gray_frame(capture)
            # Getting the ASCII frame
            ascii_frame = cam.get_ascii_frame(
                normal_frame, gray_frame, color=False)
            # Saving the ASCII frame
            cam.save_ascii_image(ascii_frame, f'{owner_id}.png')

            if self.speak:
                os.system(
                    f"""say "C'est bon, j'ai enregistré ta photo sous le nom de {owner_id}.png ! Maintenant, je vais l'envoyer à la base de données !" """)

            # Adding the ASCII frame to the database
            db = Database()
            # Adding the ASCII frame to the database
            db.add_pyxpic(DatabaseUtils.create_random_pyxpic_id(
            ), owner_id, ascii_frame)

            if self.speak:
                os.system(
                    """say "C'est bon, j'ai envoyé ta photo à la base de données !" """)
                os.system(
                    """say "Passe une bonne journée ! Et n'oublie pas de me montrer ta carte de cantine demain !" """)
            time.sleep(10)


if __name__ == "__main__":
    app = App()
    app.run()
