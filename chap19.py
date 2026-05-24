# finding the coordinates of any image or video 

import cv2 as cv
import numpy as np



# define the mouse callback function to get the coordinates of the mouse click


def get_coordinates(event, x, y, flags, param):
    
    # left mouse button click event
    if event == cv.EVENT_LBUTTONDOWN:
        print(f"Coordinates: ({x}, {y})")

        # define and print on window
        font = cv.FONT_HERSHEY_SIMPLEX
        cv.putText(frame, f"({x}, {y})", (x, y), font, 0.5, (255, 20, 20), 1, cv.LINE_AA)
        matrix.append((x, y))
        # show the text on image
        cv.imshow('Image', frame)

#  for color finding we can use right mouse button click event
    if event == cv.EVENT_RBUTTONDOWN:
        b = frame[y, x, 0]
        g = frame[y, x, 1]
        r = frame[y, x, 2]

        font = cv.FONT_HERSHEY_SIMPLEX


        cv.putText(frame, f"color: ({b}, {g}, {r})", (x, y), font, 0.5, (255, 20, 20), 1, cv.LINE_AA)
        print (f"color: ({b}, {g}, {r})")
        cv.imshow('Image', frame)

        
        


def persp_transform(frame , matrix):
    point1 = np.float32([matrix[0], matrix[1], matrix[2], matrix[3]])

    size = frame.shape[:2]

    point2 = np.float32([[0, 0], [0, size[0]], [size[1], 0], [size[1], size[0]]])

    # get the perspective transformation matrix
    transform_matrix = cv.getPerspectiveTransform(point1, point2)

    result = cv.warpPerspective(frame, transform_matrix, (size[1], size[0]))

    cv.imwrite('images/auto_warp.png', result)




# final function to read and show the image

if __name__ == "__main__":
    # read the image
    frame = cv.imread('images/warp.png' , 1)

    # SHow the image
    cv.imshow('Image', frame)

    # set the mouse callback function to the window
    cv.setMouseCallback('Image', get_coordinates)


    # perspective transformation
    # First we will get the point by mouse click in matrix
    matrix = []

    cv.waitKey(0)
    cv.destroyAllWindows()

    print(matrix)
    # look like this [(146, 101), (53, 278), (440, 287), (322, 84)]

    if len(matrix) == 4:
        # if we have 4 points then we can do perspective transformation 
        persp_transform(frame, matrix)

        cv.waitKey(0)
        cv.destroyAllWindows()






    