import cv2
import time

video = cv2.VideoCapture(0)  # 0- primary inbuilt cam 1- secondary cam eg:usb cam
time.sleep(1)

while True:
    check, frame = video.read()
    # grey_frame : to reduce matrix complexity color changed to grey
    grey_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # gausian blur : to make calculations more efficient
    grey_frame_gaus = cv2.GaussianBlur(grey_frame, (21, 21), 0)

    cv2.imshow("my video", grey_frame_gaus)

    key = cv2.waitKey(1)
    if key == ord("q"):
        break

video.release()
