#Setting of Cam and vidoe

import cv2 as cv
import numpy as np


cap = cv.VideoCapture(0)


if not cap.isOpened():
    print("Error opening video stream or file")


# keys  and values for setting of cam 
# Detailed information about the keys and values can be found in the OpenCV documentation: https://docs.opencv.org/4.x/d4/d15/group__videoio__flags__base.html
cap.set(10 , 1000)
cap.set(3 , 1080)
cap.set(4 , 1920)
cap.set(11 , 100)
cap.set(5 ,100)

while cap.isOpened():
    ret , frame = cap.read()

    if ret:
        cv.imshow('video',frame)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break  
    else:
        break

cap.release()
cv.destroyAllWindows()
