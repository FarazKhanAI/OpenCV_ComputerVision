# How to draw line and shape in Python 

import cv2 as cv
import numpy as np

# Draw a white canvas
w_img = np.ones((512, 512))

b_img = np.zeros((512, 512))

c_img = np.zeros((512, 512, 3), np.uint8) * 120
# adding colors
# c_img[100:200 , 20:100] = (255, 120, 22)  # Blue


# # Draw a line
# cv.line(w_img, (0, 0), (512, 512), (0, 0, 255), thickness=5)
# cv.line(b_img, (0, 0), (512, 512), (255, 255, 255), thickness=5)
cv.line(c_img , (250 , 10) , (250 , 502),(12 , 244 , 200) , thickness=2 )
cv.line (c_img , (10 , 250) ,(502 , 250),(12 , 244 , 200) , thickness=2 )
cv.line (c_img , (10 , 10 ) , (502 , 502), (12 , 244 , 200) , thickness=2 )
cv.line (c_img , (500 , 5), (5 , 500) , (12 , 244 , 200) , thickness=2 )



# Draw a rectangle
# cv.rectangle(c_img, (100, 100), (300, 300), (0, 0, 255), cv.FILLED)

# Draw a circle
cv.circle(c_img, (250, 250), 100, (255, 170, 0), cv.FILLED)


# adding text
cv.putText(c_img, 'OpenCV', (200, 250), cv.FONT_ITALIC, 0.7, (255,0, 255), thickness=2)

# Adding text in 2 lines text : my name is faraz , i am learning opencv using single putext function
text = 'My name is Faraz\nI am learning OpenCV' 
cv.putText(c_img, text, (10, 50), cv.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), thickness=2)

cv.imshow('Black Canvas', b_img)
cv.imshow('White Canvas', w_img)
cv.imshow('Color Canvas', c_img)
cv.waitKey(0)
cv.destroyAllWindows()
