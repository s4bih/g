import cv2
import os
import numpy as np
import imutils
import pandas as pd
import pytesseract
import time
import re

image_folder='fl/images'
actual_data=pd.read_csv('fl/actual_data.csv', sep=';')
#print (actual_data)

data_to_append=[]

def process_img(image_path):
    image=cv2.imread(image_path)
    image=imutils.resize(image,width=500)
    gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    _,binary_image=cv2.threshold(gray,150,255,cv2.THRESH_BINARY)
    countours,_=cv2.findContours(binary_image,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    contours =sorted(countours,key=cv2.contourArea,reverse=True)[:30]

    for c in contours:
        peri= cv2.arcLength(c,True)
        approx= cv2.approxPolyDP(c,0.02*peri,True)
        if len(approx)==4:
            NumberPlateCnt=approx
            break
    mask = np.zeros(gray.shape,np.uint8)
    mask = cv2.drawContours(mask,[NumberPlateCnt],0,255,-1)
    new_image=cv2.bitwise_and(image,image,mask=mask)
    config=('-l eng --oem 1 --psm 3')
    detected_plate = pytesseract.image_to_string(new_image, config=config)
    print(detected_plate)
    detected_plate = detected_plate.replace(" ", "").replace("\n", "")
    detected_plate = re.sub('[^A-Za-z0-9]', '', detected_plate).upper()

    return detected_plate

for image_file in os.listdir(image_folder):
    for image_file in os.listdir(image_folder):
        if image_file.endswith(('.jpg', '.jpeg', '.png')):
            image_path = os.path.join(image_folder, image_file)
            print(image_path)

            actual_print = actual_data[actual_data['image_file'] == image_file]['actual_number_plate'].values[0]
            print(actual_print)

            if actual_print is None:
                print("Tidak ada data actual_number_plate untuk file ini")
                continue

            detected_plate = process_img(image_path)
            print('detected plate', detected_plate)
            if actual_print == detected_plate:
                print('correct')
            else:
                print('wrong')
            time.sleep(1)








