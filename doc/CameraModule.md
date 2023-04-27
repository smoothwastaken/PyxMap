# Camera.py Documentation

This documentation provides an overview of the `camera.py` file, its classes, methods, and usage.

## Table of Contents

- [Classes](#classes)
  - [Camera](#camera)
  - [CameraUtils](#camerautils)
- [Usage](#usage)
- [License](#license)

## Classes

### Camera

The `Camera` class is responsible for handling the camera and capturing frames.

#### Methods

- `__init__(self, camera_index: int = -1, scale: float = 1) -> None`

  Initializes the camera.

  - `camera_index (int, optional)`: Specify the camera index. Defaults to `-1`.
  - `scale (float, optional)`: Scale factor for the captured frames. Defaults to `1`.

- `capture(self) -> cv2.VideoCapture`

  Captures the frame from the camera.

  - Returns: `cv2.VideoCapture`: The frame.

- `get_normal_frame(self, capture: cv2.VideoCapture) -> cv2.VideoCapture`

  Gets the frame from the camera.

  - `capture (cv2.VideoCapture)`: The capture object.
  - Returns: `cv2.VideoCapture`: The frame.

- `get_gray_frame(self, capture: cv2.VideoCapture) -> cv2.VideoCapture`

  Gets the gray frame from the camera.

  - `capture (cv2.VideoCapture)`: The capture object.
  - Returns: `cv2.VideoCapture`: The gray frame.

- `get_ascii_frame(self, normal_frame: cv2.VideoCapture, gray_frame: cv2.VideoCapture, color: bool = True) -> str`

  Gets the ASCII frame from the camera.

  - `normal_frame (cv2.Frame)`: The normal frame.
  - `gray_frame (cv2.Frame)`: The gray frame.
  - `color (bool, optional)`: If the ASCII frame should be colored. Defaults to `True`.
  - Returns: `str`: The ASCII frame.

- `save_ascii_image(self, ascii_frame: str, file_name: str = "ascii_image") -> None`

  Saves the ASCII frame as an image using Pillow (PIL).

  - `ascii_frame (str)`: The ASCII frame.
  - `file_name (str, optional)`: The file name. Defaults to `"ascii_image"`.

### CameraUtils

The `CameraUtils` class is a collection of utility functions for the `Camera` class.

#### Methods

- `get_color_escape(r: int, g: int, b: int, background: bool = False) -> str`

  Gets the escape sequence for a color.

  - `r (int)`: Level of red.
  - `g (int)`: Level of green.
  - `b (int)`: Level of blue.
  - `background (bool, optional)`: Whether to use the background color. Defaults to `False`.
  - Returns: `str`: The escape sequence.

- `list_cameras() -> list`

  Lists all available cameras using OpenCV.

  - Returns: `list`: List of cameras.

- `convert_ascii(pixel: int) -> str`

  Converts a pixel value to an ASCII character.

  - `pixel (int)`: The pixel value.
  - Returns: `str`: The ASCII character.

- `get_window_size() -> tuple`

  Gets the size of the terminal window.

  - Returns: `tuple`: The number of rows and columns of the terminal window.

- `string_to_dict(input_string: str) -> dict`

  Converts a string to a dictionary.

  - `input_string (str)`: The string to convert.
  - Returns: `dict`: The string converted to a dictionary.

- `rgb_to_hex(rgb: int) -> str`

  Converts an RGB value to a HEX value.

  - `rgb (int)`: The RGB value.
  - Returns: `str`: The HEX value.

- `clear_line(n: int = 1)`

  Clears the specified number of lines in the terminal.

  - `n (int, optional)`: Number of line(s) to clear. Defaults to `1`.

## Usage

Here's an example of how to use the `Camera` class:

```python
from camera import Camera

# Initialize the camera with a scale factor of 5.
cam = Camera(scale=5)

# Capture the frame.
capture = cam.capture()

# Get the normal and gray frames.
normal_frame = cam.get_normal_frame(capture)
gray_frame = cam.get_gray_frame(capture)

# Get the ASCII frame without color.
ascii_frame = cam.get_ascii_frame(normal_frame, gray_frame, color=False)

# Print the ASCII frame.
print(ascii_frame)

# Save the ASCII frame as an image.
cam.save_ascii_image(ascii_frame, 'test_cam_module.png')
```

This example will capture a frame using the camera, convert it to an ASCII frame, print it in the terminal, and save it as an image.

## License

This program is free software under the terms of the GNU General Public License v3.0.