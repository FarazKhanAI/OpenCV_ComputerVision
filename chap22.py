# Face detection in images
from cv2 import imwrite
import cv2 as cv


# Load Haar cascade for face detection
face_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')



img = cv.imread(r'images\peopleFaces.jpeg')
img = cv.resize(img, (img.shape[1]//2, img.shape[0]//2))

print("Image shape:", img.shape)



# Detect faces
faces = face_cascade.detectMultiScale(img, scaleFactor=1.1, minNeighbors=8)

# Draw rectangles around detected faces
for (x, y, w, h) in faces:
    cv.rectangle(img, (x, y), (x + w, y + h), (255, 0, 255), 2)


# SHow the image with detected faces

# img = cv.resize(img, (img.shape[1]//2, img.shape[0]//2))


cv.imwrite('images/detected_faces.jpg', img)  # Save the image with detected faces

cv.imshow('Image', img)
cv.waitKey(0)
cv.destroyAllWindows()