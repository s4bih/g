import cv2
import numpy as np
import matplotlib.pyplot as plt

image_part='bata.jpg'
original = cv2.imread(image_part)
cv2.imshow('image', original)
height, width = original.shape[:2]
scale= 600/max(height, width)

image = cv2.resize(original, (int(width*scale), int(height*scale)))

image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

histogram = cv2.calcHist([image], [0], None, [256], [0, 256])

plt.plot(histogram)
plt.title('histogram')
plt.xlim([0, 256])
plt.ylabel('number of pixels')
plt.xlabel('intensity')
plt.grid(True)
plt.show()