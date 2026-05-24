# Detect specific color using HSV sliders

import cv2 as cv
import numpy as np

# Load image
path = r'images\image.jpg'

img = cv.imread(path)

if img is None:
    print("Error: Could not load image")
    exit()

# Resize image (optional)
img = cv.resize(img, (600, 400))

# Convert to HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

# Empty callback function
def slider(x):
    pass

# Create window
cv.namedWindow("Bars")
cv.resizeWindow("Bars", 640, 240)

# Create trackbars
cv.createTrackbar("Hue Min", "Bars", 0, 179, slider)
cv.createTrackbar("Hue Max", "Bars", 179, 179, slider)

cv.createTrackbar("Sat Min", "Bars", 0, 255, slider)
cv.createTrackbar("Sat Max", "Bars", 255, 255, slider)

cv.createTrackbar("Val Min", "Bars", 0, 255, slider)
cv.createTrackbar("Val Max", "Bars", 255, 255, slider)

while True:

    # Get trackbar values
    h_min = cv.getTrackbarPos("Hue Min", "Bars")
    h_max = cv.getTrackbarPos("Hue Max", "Bars")

    s_min = cv.getTrackbarPos("Sat Min", "Bars")
    s_max = cv.getTrackbarPos("Sat Max", "Bars")

    v_min = cv.getTrackbarPos("Val Min", "Bars")
    v_max = cv.getTrackbarPos("Val Max", "Bars")

    # Lower and upper HSV range
    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])

    # Create mask
    mask = cv.inRange(hsv, lower, upper)

    # Apply mask to original image
    result = cv.bitwise_and(img, img, mask=mask)

    # Show images
    cv.imshow("Original", img)
    cv.imshow("Mask", mask)
    cv.imshow("Result", result)

    # Press q to quit
    key = cv.waitKey(1)

    if key == ord('q'):
        break

# Cleanup
cv.destroyAllWindows()