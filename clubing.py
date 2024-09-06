import cv2
import numpy as np
image1 = cv2.imread('bata.jpg')
image = cv2.imread('307.jpg')
def combine_images(image1, image):
    if image1.shape!=image.shape:
        image1 = cv2.resize(image1, (image.shape[1], image.shape[0]))
    combine_image = (image + image1)/2
    combine_image = np.maximum(image, image1)
    alpha = 0.5
    combine_image = cv2.addWeighted(image, alpha, image1, 1 - alpha, 0)
    concanated = np.vstack((image1, combine_image))


    print(image1.shape)
    print(image1.shape[1])
    print (image1.shape[0])
    print(image.shape)
    cv2.imshow('combined', concanated)
    cv2.imshow('baru', combine_image)
    cv2.imshow('original', image1)
    cv2.imshow('original2', image)



    #v_combined = cv2.vconcat([image1, image])

    #cv2.imshow('combined', v_combined)
    cv2.waitKey(0)
combine_images(image1, image)