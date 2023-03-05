#	made by Lucas Schmirl 20.02.2022,	last edit: 20.02.2022
import cv2
import numpy as np


## Look into "README.md" why this is not working!

all_camera_idx_available = []

for camera_idx in range(10):
    cap = cv2.VideoCapture(camera_idx)
    if cap.isOpened():
        print(f'Camera index available: {camera_idx}')
        all_camera_idx_available.append(camera_idx)
        cap.release()