import cv2
from pyzbar import pyzbar


class QRCode(object):
    def __init__(self) -> None:
        pass


    def read(self, file: str = None, camera: int = 0):
        """This function allows to read QR Codes.

        Args:
            file (str, optional): Pass the path to the image that you want to scan. If not set, using camera. Defaults to None.
            camera (int, optional): Pass the camera number that CV2 module will use to scan a QR Code. Defaults to 0.
        """
        # 
        if file:
            # qr.decode(file)
            print(qr.data)
        else:
            cap = cv2.VideoCapture(camera)
            while True:
                ret, frame = cap.read()
                barcodes = pyzbar.decode(frame)
                for barcode in barcodes:
                    x, y , w, h = barcode.rect
                    #1
                    barcode_info = barcode.data.decode('utf-8')
                    cv2.rectangle(frame, (x, y),(x+w, y+h), (0, 255, 0), 2)
                    #2
                    font = cv2.FONT_HERSHEY_SIMPLEX
                    cv2.putText(frame, barcode_info, (x + 6, y - 15), font, 2.0, (255, 255, 255), 1)
                    print(barcode_info)
                    #3
                    with open("barcode_result.txt", mode ='w') as file:
                        file.write("Recognized Barcode:" + barcode_info)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
                cv2.imshow('Camera', frame)
                # return frame
            cap.release()
            cv2.destroyAllWindows()

if __name__ == "__main__":
    qr = QRCode()
    qr.read()