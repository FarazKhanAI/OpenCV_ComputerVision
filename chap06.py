# reading a video and displaying it

import cv2 as cv
import numpy as np

cap = cv.VideoCapture(r'CV\images\video.mp4')

# Indicate if the video is opened successfully or not
if not cap.isOpened():
    print("Error opening video stream or file")
   
while cap.isOpened():
    ret, frame = cap.read()
    # Convert the video to grey video
    # frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    if ret:
        cv.imshow('Video', frame)
        if cv.waitKey(25) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
cv.destroyAllWindows()  
