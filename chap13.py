# Basic function and manipulation in CV

from cv2 import dilate
import cv2 as cv
import numpy as np

img = cv.imread(r'images\image.jpg')

if img is None:
    print('Could not read the image.')
    exit()

# Resize the image to a specific width and height
# resized_img = cv.resize(img, (150, 250))

# cv.imshow('Resized Image', resized_img)
# # Convert the image to grayscale
# gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Grayscale Image', gray_img)


# blur the image using a Gaussian blur
# blurred_img = cv.GaussianBlur(img, (15, 15), 0)
# cv.imshow('Blurred Image', blurred_img)

img = cv.resize(img, (600,400))

# Edge detection using Canny edge detector
# edge_img = cv.Canny(img, 48,48)
# cv.imshow('Edge Detected Image', edge_img)

# thickness of the edges
# create own kernel for dilation
# matrix = np.ones((2, 2), dtype=np.uint8)
# dilated_img = dilate(edge_img, matrix, iterations=1)
# cv.imshow('Dilated Image', dilated_img)


# # Erosion to thin the edges
# eroded_img = cv.erode(dilated_img, matrix, iterations=1)
# cv.imshow('Eroded Image', eroded_img)



# Black and white image using thresholding
# grey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# _, thresholded_img = cv.threshold(grey, 127, 255, cv.THRESH_BINARY)

# neg_img = ~(thresholded_img)
# cv.imshow('Thresholded Image', neg_img)


# Crop the image using array slicing 
cropped_img = img[100:300, 200:400]
cv.imshow('Cropped Image', cropped_img)



# Display the image
cv.imshow('Image', img)
# Wait until a key is pressed and close the window
cv.waitKey(0)
cv.destroyAllWindows()





