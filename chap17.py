# joining 2 images
import cv2 as cv
import numpy as np

# Load images
img1 = cv.imread(r'images/image_copy.jpg')

# stacking same image horizontally and vertically
h_stack = np.hstack((img1, img1))
v_stack = np.vstack((img1, img1))


# Display the stacked images
cv.imshow('Horizontal Stack', h_stack)
cv.imshow('Vertical Stack', v_stack)


# Limitations of stacking
# 1. The images must have the same number of channels (e.g., both should be color images or both should be grayscale).
# 2. The images must have the same dimensions (width and height) for stacking to work properly. If the images have different sizes, you may need to resize them before stacking.    






cv.waitKey(0)
cv.destroyAllWindows()
