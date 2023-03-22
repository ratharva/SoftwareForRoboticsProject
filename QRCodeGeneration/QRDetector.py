import qrcode
import uuid
import cv2

print(cv2.__version__)

myImg = cv2.imread("./TempQr.png")

myQrDetector = cv2.QRCodeDetector()

# retval, decoded_info, points, straight_qrcode = myQrDetector.detectAndDecodeMulti(myImg)
# print("Retval", retval)
# print("decoded_info", decoded_info)
# print("points", points)
# print("straight_qrcode", straight_qrcode)


camera_id = 0
delay = 1
window_name = 'OpenCV QR Code'

cap = cv2.VideoCapture(camera_id)

while True:
    ret, frame = cap.read()

    if ret:
        ret_qr, decoded_info, points, _ = myQrDetector.detectAndDecodeMulti(frame)
        if ret_qr:
            for s, p in zip(decoded_info, points):
                if s:
                    print(s)
                    color = (0, 255, 0)
                else:
                    color = (0, 0, 255)
                frame = cv2.polylines(frame, [p.astype(int)], True, color, 8)
        cv2.imshow(window_name, frame)

    if cv2.waitKey(delay) & 0xFF == ord('q'):
        break

cv2.destroyWindow(window_name)