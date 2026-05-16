# image saving or image writing

import cv2 as cv
import numpy as np


# image read
img = cv.imread(r'CV\images\image.jpg')
img = cv.resize(img, (600, 400))


# Convert to grey image
gray = cv.cvtColor(img , cv.COLOR_BGR2GRAY)

# save the image
cv.imwrite(r'CV\images\grey_image.jpg', gray)


# show the image
cv.imshow('Grey Image', gray)

cv.waitKey(0)
cv.destroyAllWindows()

