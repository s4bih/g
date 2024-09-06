import cv2
import numpy as np

drawing = False
point=[]
mask = None

koi='307.jpg'

image = cv2.imread(koi)

def draw_freehand(event, x, y, flags, param):
    global point, drawing, mask
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        point = [(x, y)]
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        point.append((x, y))
        cv2.fillPoly(mask, np.array([point]), (255, 255, 255))
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:

            point.append((x, y))

mask=np.zeros_like(image)

cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_freehand)

while True:
    cv2.imshow('image', cv2.addWeighted(image, 0.5, mask, 0.5, 0))
    key = cv2.waitKey(1) & 0xFF
    if key == ord('x'):
        mask = np.zeros_like(image)
    elif key == 27:
        break
selected_area = cv2.bitwise_and(image, mask)


cv2.imshow("selected area", selected_area)
cv2.waitKey(0)
cv2.destroyAllWindows()


