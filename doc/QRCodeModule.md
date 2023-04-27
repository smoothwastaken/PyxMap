# QRCode.py Documentation

This documentation provides an overview of the `qrcode.py` file, its class, methods, and usage.

## Table of Contents

- [Class](#class)
  - [QRCode](#qrcode)
- [Usage](#usage)
- [License](#license)

## Class

### QRCode

The `QRCode` class is responsible for reading QR Codes using a camera or an image file.

#### Methods

- `__init__(self) -> None`

  Initializes the QRCode class.

- `read(self, file: str = None, camera: int = 0, showCameraWindow: bool = False) -> None`

  Reads QR Codes using a camera or an image file.

  - `file (str, optional)`: Pass the path to the image that you want to scan. If not set, using the camera. Defaults to `None`.
  - `camera (int, optional)`: Pass the camera number that CV2 module will use to scan a QR Code. Defaults to `0`.
  - `showCameraWindow (bool, optional)`: Whether to display the camera window while scanning. Defaults to `False`.

  - Returns: `str`: The decoded QR Code information.

## Usage

Here's an example of how to use the `QRCode` class:

```python
from qrcode import QRCode
from camera import CameraUtils

# Initialize the QRCode class.
qr = QRCode()

# Read the QR Code using the first available camera.
result = qr.read(camera=CameraUtils.list_cameras()[0])

# Print the decoded QR Code information.
print(result)
```

This example will capture a QR Code using the camera, decode it, and print the decoded QR Code information.

## License

This program is free software under the terms of the GNU General Public License v3.0.
