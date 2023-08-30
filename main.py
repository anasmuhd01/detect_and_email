import cv2
import time

video = cv2.VideoCapture(0)  # 0- primary inbuilt cam 1- secondary cam eg:usb cam
time.sleep(1)

while True:
    check, frame = video.read()
    cv2.imshow("my video", frame)

    key = cv2.waitKey(1)
    if key == ord("q"):
        break

video.release()
