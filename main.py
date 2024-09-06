import cv2
import numpy as np
image = 'bata.jpg'

image_path=cv2.imread(image)

clone = image_path.copy()

(x1,y1, x2,y2) = cv2.selectROI("select roi", image_path, fromCenter=False, showCrosshair=False)

selected_area = clone[y1:y1+y2, x1:x1+x2]

cv2.imshow("selected area", selected_area)

cv2.waitKey(0)
