import cv2
import numpy as np
from ultralytics import YOLO

model=YOLO('yolov8n.pt')

video="burung.mp4"
cap = cv2.VideoCapture(video)

while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        result=model(frame  )
        annoted_image=result[0].plot()

        cv2.imshow('annoted image', annoted_image)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    else:
        break

cap.release()
cv2.destroyAllWindows()

