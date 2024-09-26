import cv2
import numpy as np

image = 'wajah.jpg'

image_path = cv2.imread(image)

color_ranges = {
    'red': ((0, 0, 255), (0, 0, 255)),
    'green': ((0, 255, 0), (0, 255, 0)),
    'blue': ((255, 0, 0), (255, 0, 0)),
    'yellow': ((0, 255, 255), (0, 255, 255)),
    'black': ((0, 0, 0), (0, 0, 0)),
    'white': ((255, 255, 255), (255, 255, 255))
}
color=input("masukkan warna : ")

def detect_color(image,lower_color, upper_color):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    mask = cv2.inRange(hsv, lower_color, upper_color)
    result=cv2.bitwise_and(image, image, mask=mask)
    return result

if color not in color_ranges.keys():
    print("Warna tidak ditemukan")
    exit()
elif color in color_ranges.keys():
    print("Warna ditemukan")
    resul = detect_color(image_path, np.array(color_ranges[color][0]), np.array(color_ranges[color][1]))
    cv2.imshow('image', image_path)

    cv2.imshow('resul', resul)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


