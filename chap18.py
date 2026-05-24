# How to change the perpective of an image using OpenCV
import cv2 as cv
import numpy as np

img = cv.imread(r'images/warp.png')




print(img.shape)


# Definig the points for perspective transformation
p1 = np.float32([[145, 101], [50, 279] , [322, 84],  [442, 287]])

width , hight = 497 , 561
  

p2 = np.float32([[0, 0], [0, hight], [width, 0], [width, hight]])



matrix = cv.getPerspectiveTransform(p1, p2)

result = cv.warpPerspective(img, matrix, (width, hight))
cv.imshow("Result", result)


#  Write the result image 

cv.imwrite('images/warp_result.png', result)




cv.waitKey(0)
cv.destroyAllWindows()