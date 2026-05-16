#Open CV  -> Read and Show Image 

import cv2 as cv
import numpy as np

i = cv.imread(r'CV\images\image.jpg' , cv.IMREAD_GRAYSCALE) #read image in grayscale mode
#show image
print(i)
cv.imshow('Image', i)
cv.waitKey(0) #wait until any key is pressed