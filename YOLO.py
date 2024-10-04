import cv2
from ultralytics import YOLO

iamge = 'dog-facts-cat-facts.webp'
model = YOLO('yolov8n.pt')
results = model.predict(source=iamge, show=True,conf=0.5,save=False)
results=results[0]


print(results.names)
print(len(results.boxes))

for box in results.boxes:
    class_id = results.names[box.cls[0].item()]
    cord = box.xyxy[0].tolist()
    cord = [round(x) for x in cord]
    conf=box.conf[0].item(),2

    #detail
    print("object type:", class_id)
    print("confidence:", conf)
    print("coordinates:", cord)
    print("\n")

    if conf > 0.5:
        x1,y1,x2,y2 = cord
        image=cv2.rectangle(image,(x1,y1),(x2,y2),(0,255,0),3)
        label = f"{class_id} {conf}"
        image=cv2.putText(image,label,(x1,y1-10),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,255,0),2)





