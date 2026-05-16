#Resize an image using OpenCV the resize() function. The resize() function takes two arguments: the source image and the desired size of the output image. The desired size is specified as a tuple of (width, height). For example, to resize an image to 600x800 pixels, you can use the following code:


import cv2 as cv
import numpy as np

i = cv.imread(r'CV\images\image.jpg')
i2 = i.copy()
#resize the image to 600x800 pixels
i = cv.resize(i, (600,600))

# show the image
cv.imshow('original image', i2)
cv.imshow('resize image', i)
# wait for a key press and close the window
cv.waitKey(0)
cv.destroyAllWindows()