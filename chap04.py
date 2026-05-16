# convert image to black and white image 

import cv2 as cv
import numpy as np

# image read 
img = cv.imread(r'CV\images\image.jpg')

img = cv.resize(img, (600, 400))

# convert to black and white image
grey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
(thresh, b_w) = cv.threshold(grey, 127, 255, cv.THRESH_BINARY)

# Convert to black and white image to negative image
negative = cv.bitwise_not(b_w)

# show the image
cv.imshow('Original Image', img)
cv.imshow('Black and White Image', b_w)
cv.imshow('Negative Image', negative)


# 
cv.waitKey(0)       
cv.destroyAllWindows()
