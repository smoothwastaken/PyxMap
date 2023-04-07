import cv2
from pyzbar import pyzbar


class QRCode(object):
    def __init__(self) -> None:
        pass

    def read(self, file: str = None, camera: int = 0, showCameraWindow: bool = False) -> None:
        """This function allows to read QR Codes.

        Args:
            file (str, optional): Pass the path to the image that you want to scan. If not set, using camera. Defaults to None.
            camera (int, optional): Pass the camera number that CV2 module will use to scan a QR Code. Defaults to 0.
        """

        # Initialize the barcode information.
        barcode_info = None

        while barcode_info == None:

            # Read the camera or the image.
            cap = cv2.VideoCapture(camera)
            ret, frame = cap.read()

            # Decode the QR Code.
            barcodes = pyzbar.decode(frame)

            # Loop over all detected barcodes.
            for barcode in barcodes:
                x, y, w, h = barcode.rect

                # The barcode data is a bytes object so we convert it to a string.
                barcode_info = barcode.data.decode('utf-8')

                # Draw the barcode area in the image.
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

                # Draw the barcode data and barcode type on the image.
                font = cv2.FONT_HERSHEY_SIMPLEX
                cv2.putText(frame, barcode_info, (x + 6, y - 15),
                            font, 2.0, (255, 255, 255), 1)

                # Print the barcode type and data to the terminal.
                with open("barcode_result.txt", mode='w') as file:
                    file.write("Recognized Barcode:" + barcode_info)

            # If the user presses "q", quit.
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

            # Show the camera window if the user wants to.
            if showCameraWindow:
                cv2.imshow('Camera', frame)

            # Release the camera and close all windows.
            cap.release()
            cv2.destroyAllWindows()

        # Return the barcode information.
        return barcode_info


if __name__ == "__main__":
    qr = QRCode()
    qr.read(0)
