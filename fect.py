import cv2
import numpy as np
import threading
import queue
from ultralytics import YOLO

model=YOLO('yolov8n.pt')
model1=YOLO('yolov8n-seg.pt')

video="burung.mp4"
video1="burunj.mp4"

frame_queue=queue.Queue()
frame_queue1=queue.Queue()
def run(filename,frame_queue,model):
    vido=cv2.VideoCapture(filename)
    frames=int(vido.get(cv2.CAP_PROP_FRAME_COUNT))
    for _ in range(frames):
        ret, frame = vido.read()
        if ret:
            result=model.track(source=frame)
            res_plo=result[0].plot()
            frame_queue.put(res_plo)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        else:
            break
    vido.release()
traker=threading.Thread(target=run,args=(video,frame_queue,model))
traker1=threading.Thread(target=run,args=(video1,frame_queue1,model1))
traker.start()
traker1.start()

while True:
    if frame_queue.qsize()>0:
        frame=frame_queue.get()
        cv2.imshow('annoted image', frame_queue.get())
    if frame_queue1.qsize()>0:
        frame=frame_queue1.get()
        cv2.imshow('annoted image', frame_queue1.get())
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()