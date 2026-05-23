#Resolution of cam 

import cv2 as cv
import numpy as np


cap = cv.VideoCapture(0)



# cap.set(cv.CAP_PROP_FRAME_WIDTH, 640)

def HD_res():
        # resolution HD
    cap.set(cv.CAP_PROP_FRAME_WIDTH, 1280)
    cap.set(cv.CAP_PROP_FRAME_HEIGHT, 720)
    

def SD_res():
        # resolution SD
    cap.set(cv.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv.CAP_PROP_FRAME_HEIGHT, 480)

def FullHD_res():   
        # resolution Full HD
    cap.set(cv.CAP_PROP_FRAME_WIDTH, 1920)
    cap.set(cv.CAP_PROP_FRAME_HEIGHT, 1080)


# SD_res()
# HD_res()
# how to fix the frame rate to 30 fps
cap.set(cv.CAP_PROP_FPS, 60)

while True:
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    # gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    # Edge detection
    edges = cv.Canny(frame, 80, 80)
    # Dilate the edges
    kernel = np.ones((3, 3), dtype=np.uint8)
    edges = cv.dilate(edges, kernel, iterations=1)

    cv.imshow('frame', frame)
    cv.imshow('edges', edges)
    
    if cv.waitKey(1) == ord('q'):
        break

cap.release()
cv.destroyAllWindows()