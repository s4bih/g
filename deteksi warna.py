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


def color_detection(image_path, lower_color, upper_color):
    image = cv2.imread(image_path)
    if image is None:
        print("Error: Could not load image")
        return None
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv_image, lower_color, upper_color)
    result = cv2.bitwise_and(image, image, mask=mask)
    return result



if color in color_ranges.keys():
    result = color_detection(image, np.array(color_ranges[color][0]), np.array(color_ranges[color][1]))

    cv2.imshow('original image', image_path)

    cv2.imshow('result', result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("color not found")

