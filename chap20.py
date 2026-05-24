# split vidoe into frames

import cv2 as cv
import numpy as np

# Open the video file
cap = cv.VideoCapture(r'images\video.mp4')

if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

frame_count = 0
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("End of video reached or cannot read the frame.")
        break
    frame_count += 1
    if frame_count % 100 == 0:  
        # Save every 100th frame (adjust as needed)
        cv.imwrite(f'images/video_Frames/frame_{frame_count:04d}.jpg', frame)
    
        
    
    
    # Display the frame (optional)

print(f"Total frames extracted: {frame_count}")

# Release the video capture object
cap.release()
