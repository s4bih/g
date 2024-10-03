import cv2
import numpy as np
import matplotlib.pyplot as plt

image_part='wajah.jpg'
original = cv2.imread(image_part)
height, width = original.shape[:2]
scale= 600/max(height, width)

image = cv2.resize(original, (int(width*scale), int(height*scale)))
red_histogram = cv2.calcHist([image], [0], None, [256], [0, 256])
blue_histogram = cv2.calcHist([image], [1], None, [256], [0, 256])
green_histogram = cv2.calcHist([image], [2], None, [256], [0, 256])


plt.figure(figsize=(10, 5))
plt.subplot(3,1,1)
plt.plot(red_histogram,color='r')
plt.title('red histogram')

plt.subplot(3,1,2)
plt.plot(blue_histogram,color='b')
plt.title('blue histogram')

plt.subplot(3,1,3)
plt.plot(green_histogram,color='g')
plt.title('green histogram')

plt.show()
plt.tight_layout()