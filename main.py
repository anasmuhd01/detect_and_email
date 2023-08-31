import cv2
import time

video = cv2.VideoCapture(0)  # 0- primary inbuilt cam 1- secondary cam eg:usb cam
time.sleep(1)

first_frame = None

while True:
    check, frame = video.read()

    # grey_frame : to reduce matrix complexity color changed to grey
    # gausian blur : to make calculations more efficient
    grey_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    grey_frame_gaus = cv2.GaussianBlur(grey_frame, (21, 21), 0)

    if first_frame is None:
        first_frame = grey_frame_gaus

# delta_frame compares the first_frame with grey_frame_gaus when object appears color changes
    delta_frame = cv2.absdiff(first_frame, grey_frame_gaus)
    cv2.imshow("my video", delta_frame)

    key = cv2.waitKey(1)
    if key == ord("q"):
        break

video.release()
