import cv2
import numpy as np

image=cv2.imread('bata.jpg')
cv2.namedWindow('eye')

color_ranges = {
    'red': ((0, 0, 255), (0, 0, 255)),
    'green': ((0, 255, 0), (0, 255, 0)),
    'blue': ((255, 0, 0), (255, 0, 0)),
    'yellow': ((0, 255, 255), (0, 255, 255)),
    'black': ((0, 0, 0), (0, 0, 0)),
    'white': ((255, 255, 255), (255, 255, 255))
}

def get_color(hue_value):
    for color_name, (lower, upper) in color_ranges.items():
        if lower[0] <= hue_value <= upper[0] :

            return color_name

def mouse(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        b, g, r = image[y, x]
        print("warnai", image[y,x])
        color_window = np.zeros((100, 100, 3), np.uint8)
        color_window[:] = [b, g, r]
        cv2.imshow("color", color_window)
        hsv_frame = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        color_heu=hsv_frame[y, x,0]
        color_name=get_color(color_heu)
        print(color_name)

cv2.setMouseCallback('eye', mouse)



while True:
    cv2.imshow('eye', image)
    key=cv2.waitKey(1)
    if key==ord('q'):
        break
cv2.destroyAllWindows()