import cv2 as cv
import threading

# Load Haar cascade
face_cascade = cv.CascadeClassifier(
    cv.data.haarcascades + 'haarcascade_frontalface_default.xml'
)

# Open video
cap = cv.VideoCapture(r'images\people.mp4')

if not cap.isOpened():
    print("Cannot open video")
    exit()

# Shared faces variable
faces = []

# Detection function
def detect_faces(gray_frame):

    global faces

    detected = face_cascade.detectMultiScale(
        gray_frame,
        scaleFactor=1.1,
        minNeighbors= 7
    )

    faces = detected


# Resize helper
def resize_frame(frame, scale=0.5):

    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    return cv.resize(frame, (width, height))


frame_count = 0

while True:

    ret, frame = cap.read()

    if not ret:
        print("Video ended")
        break

    # Resize for speed
    frame = resize_frame(frame, 0.5)

    frame_count += 1

    # Run detection every 5th frame
    if frame_count % 5 == 0:

        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

        # Start detection thread
        threading.Thread(
            target=detect_faces,
            args=(gray,),
            daemon=True
        ).start()

    # Draw faces
    for (x, y, w, h) in faces:

        cv.rectangle(
            frame,
            (x, y),
            (x + w, y + h),
            (255, 0, 255),
            2
        )

    cv.imshow("Video", frame)

    if cv.waitKey(25) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()