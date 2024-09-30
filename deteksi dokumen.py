import cv2
import tkinter as tk
from tkinter import filedialog
import numpy as np

root = tk.Tk()
root.withdraw()

image = filedialog.askopenfilename(title="Select image", filetypes=[("image", ".jpg"),("all files", "*.*")])
image_path = cv2.imread(image)

point=[]
dots=None
imaget=None

def draw_dots(event, x, y, flags, param):
    global point
    if event == cv2.EVENT_LBUTTONUP:
        if len(point)<4:
            point.append((x, y))
            cv2.circle(dots,(x, y), 3, (0, 0, 255), -1)
            print(point)
            if len(point) == 4:
                warped_image = four_point_transform(original.copy(),np.array(point))
                cv2.imshow("warped", warped_image)

def four_point_transform(image, pts):
    rect = order_points(pts)



def order_points(pts):
    rect = np.zeros((4, 2), dtype = "float32")
    s = pts.sum(axis = 1)
    rect[0] = pts[np.argmin(s)]
    rect[2] = pts[np.argmax(s)]
    diff = np.diff(pts, axis = 1)
    rect[1] = pts[np.argmin(diff)]
    rect[3] = pts[np.argmax(diff)]
    return rect



if image != "":
    global imaget
    original = cv2.imread(image)
    height, width = original.shape[:2]
    scale= 600/max(height, width)
    imageresize = cv2.resize(original, None, fx=scale, fy=scale, interpolation=cv2.INTER_LINEAR)
    dots=np.zeros_like(imageresize)

    cv2.namedWindow('image')
    cv2.setMouseCallback('image', draw_dots)

    while True:
        image_combined = cv2.addWeighted(imageresize, 0.5, dots, 0.5, 0)
        cv2.imshow('image', cv2.addWeighted(imageresize, 0.5, dots, 0.5, 0))

        key = cv2.waitKey(1) & 0xFF
        if key == ord('x'):
            break









cv2.waitKey(0)
cv2.destroyAllWindows()