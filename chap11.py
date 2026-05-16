# capture the video from the webcam and save it to a file

import cv2 as cv

cap = cv.VideoCapture(0)

# Define the codec and create VideoWriter object
fourcc = cv.VideoWriter_fourcc(*'mp4v')
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
out = cv.VideoWriter(r'CV\images\stream.mp4', fourcc, 20.0, (frame_width, frame_height) , isColor=False)


if not cap.isOpened():
    print("Error opening video stream or file") 
while cap.isOpened():
    r , f = cap.read()
    g_f = cv.cvtColor(f, cv.COLOR_BGR2GRAY)

    if r:
        out.write(g_f)
        cv.imshow('webcam',g_f)
        cv.imshow('original',f)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break  
    else:
        break


cap.release()
out.release()
cv.destroyAllWindows()