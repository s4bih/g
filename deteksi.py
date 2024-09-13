import cv2
import numpy as np

from photo import videoCapture, output_video, output_video_path


def detect_face():
    image = 'wajah.jpg'

    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    image_pat = cv2.imread(image)

    gray = cv2.cvtColor(image_pat, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    for (x, y, w, h) in faces:
        cv2.rectangle(image_pat, (x, y), (x + w, y + h), (255, 0, 0), 2)

    cv2.imshow('image', image_pat)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
#detect_face()

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
video_Capture = cv2.VideoCapture(0)
fps = int(videoCapture.get(cv2.CAP_PROP_FPS))
width = int(videoCapture.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(videoCapture.get(cv2.CAP_PROP_FRAME_HEIGHT))
output_video_path = output_video
output_video = cv2.VideoWriter(output_video, cv2.VideoWriter_fourcc(*'mp4v'), fps, (width, height))

while True:

    ret, frame = video_Capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_Capture.release()
cv2.destroyAllWindows()


output_video_path = output_video