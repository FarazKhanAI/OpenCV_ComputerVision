# Saving HD recording of cam

import cv2 as cv
import numpy as np

# cam
cap = cv.VideoCapture(0)


def HD_res():
    return cap.set(cv.CAP_PROP_FRAME_WIDTH, 1280) and cap.set(cv.CAP_PROP_FRAME_HEIGHT, 720)

    
HD_res()


# Define the codec and create VideoWriter object

# Define the codec and create VideoWriter object

frame_width = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))
fourcc = cv.VideoWriter_fourcc(*'mp4v')  # Codec for .mp4 files
out = cv.VideoWriter('images/edges.mp4', fourcc, 20.0, (frame_width, frame_height), isColor=False)  # Output file, codec, fps, frame size, isColor




if not cap.isOpened():
    print("Cannot open camera")
    exit()

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    # Write the frame to the output file
    edges = cv.Canny(frame, 80, 80) 

    out.write(edges)

    cv.imshow('frame', frame)
    cv.imshow('edges', edges)
    if cv.waitKey(1) == ord('q'):
        break

# Release everything
cap.release()
out.release()
cv.destroyAllWindows()