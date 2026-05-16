# Convert the WEBCAM video to grey video

import cv2 as cv

cap = cv.VideoCapture(0)

if not cap.isOpened():
    print("Error opening video stream or file") 

while cap.isOpened():
    r , f = cap.read()

    g_f = cv.cvtColor(f, cv.COLOR_BGR2GRAY)
    # t , bw = cv.threshold(g_f, 127, 255, cv.THRESH_BINARY)

    # bw = cv.bitwise_not(bw)

    if r:
        cv.imshow('webcam',g_f)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break  
    else:
        break



cap.release()
cv.destroyAllWindows()