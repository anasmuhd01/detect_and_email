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

# tres_frame : to change color to pure white to catch difference
    tresh_frame = cv2.threshold(delta_frame, 60, 255, cv2.THRESH_BINARY)[1]
# del_frame : to delete the noise
    del_frame = cv2.dilate(tresh_frame, None, iterations=2)
    cv2.imshow("my video", del_frame)

# contours and green line added with rectangle
    contours , check = cv2.findContours(del_frame, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        if cv2.contourArea(contour) < 5000:
            continue
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)
    cv2.imshow("video",frame)
    key = cv2.waitKey(1)
    if key == ord("q"):
        break

video.release()
