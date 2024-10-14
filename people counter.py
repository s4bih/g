import cv2
import numpy as np
from ultralytics import YOLO

model=YOLO('yolov8x.pt')

video="banyak.mp4"
widht=640
height=480
cap = cv2.VideoCapture(video)

while True:
    people_count=set()
    ret,frame=cap.read()
    print(ret)
    if frame is None:
        print("Frame tidak dapat dibaca")
        continue
    if not ret:
        break

    rgb=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    result=model(rgb)
    for i in range(len(result[0].boxes)):
        x1,y1,x2,y2=result[0].boxes[i].xyxy[i]
        score=result[0].boxes.conf[i]
        cls=result[0].boxes.cls[i]
        ids=result[0].boxes.id[i]

        x1,y1,x2,y2,score,cls,ids=int(x1),int(y1),int(x2),int(y2),float(score),int(cls),int(ids)
        if score <0.5 or cls!=0:
            continue
        cx,cy=int(x1/2+x2/2),int(y1/2+y2/2)
        cv2.circle(frame,(cx,cy),5,(0,255,0),-1)

        people_count_text="people count:"+str(len(people_count))
        cv2.putText(frame,people_count_text,(0,height-20),1,1,(0,255,0),2)
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()





