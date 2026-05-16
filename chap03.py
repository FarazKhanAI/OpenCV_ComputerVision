#Gray scale images are single channel images that represent the intensity of light in the image. They are often used in image processing and computer vision tasks because they are simpler to work with than color images. In this code, we will convert a color image to grayscale using OpenCV.

import cv2 as cv
import numpy as np

# import the image and resize it to 400x400
img = cv.imread(r'CV\images\image.jpg' )
img = cv.resize(img, (400, 400))


# convert the image to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

#show the image 
cv.imshow('Original Image', img)
# show the grayscale image
cv.imshow('Grayscale Image', gray)
# wait until a key is pressed and close the windows
cv.waitKey(0)
cv.destroyAllWindows()

