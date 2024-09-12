import cv2
import numpy as np

image = cv2.imread('307.jpg')
image_path = 'bata.jpg'

cv2.imshow('image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

point = []
mask = np.zeros_like(image)
dots = np.zeros_like(image)
shapes = []

def draw_freehand(event, x, y, flags, param):
    global point


    if event == cv2.EVENT_LBUTTONUP:
        point.append((x, y))
        cv2.circle(dots,(x, y), 3, (0, 0, 255), -1)

    elif event == cv2.EVENT_MOUSEMOVE:...

cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_freehand)

while True:
    combined = cv2.addWeighted(image, 0.5, mask, 0.5, 0)
    combined = cv2.addWeighted(combined,0.7,dots,0.3,0)

    cv2.imshow('combined', combined)
    key = cv2.waitKey(1)
    if key==ord('x'):
        point=[]
        shapes=[]
        mask = np.zeros_like(image)
        dots = np.zeros_like(image)

    elif key==ord('c'):
        if len(point) == 2:
            radius = int(cv2.norm(np.array(point[1]) - np.array(point[0])))
            cv2.circle(mask, point[0], radius, (255, 255, 255), -1)
            circle_points = cv2.ellipse2Poly(point[0], (radius, radius), 0, 0, 360, 1)
            shapes.append(circle_points)
            dots = np.zeros_like(image)
            points = []

            # extrac and display the selected area
            cv2.fillPoly(dots, shapes, (255, 255, 255))
            selected_area = cv2.bitwise_and(image, dots)
            cv2.imshow('selected area', selected_area)
    elif key==ord('e'):...
    elif key==ord('q'):...

    elif key==ord('q'):
        break


