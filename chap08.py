# Writing the video to a file

import cv2 as cv
import numpy as np

cap = cv.VideoCapture(r'CV\images\video.mp4')

# Define the codec and create VideoWriter object
fourcc = cv.VideoWriter_fourcc(*'mp4v')
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
out = cv.VideoWriter(r'CV\images\output.mp4', fourcc, 20.0, (frame_width, frame_height) , isColor=False)

# Indicate if the video is opened successfully or not
if not cap.isOpened():
    print("Error opening video stream or file")
   
while cap.isOpened():
    ret, frame = cap.read()
    # Convert the video to grey video
    grayFrame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    if ret:
        out.write(grayFrame)
        cv.imshow('Video', grayFrame)
        if cv.waitKey(25) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
cv.destroyAllWindows()  
