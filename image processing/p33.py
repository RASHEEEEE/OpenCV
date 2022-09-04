import numpy as np
import cv2 as cv

img = cv.imread('B5.jpg')
img_small=cv.resize(img,(400,400))
cv.imshow("Original Image",img_small)
kernel = np.ones((3,3),np.uint8)
closing = cv.morphologyEx(img_small, cv.MORPH_CLOSE, kernel,iterations =2)
cv.imshow("Closing Operation with kernel(5*5)",closing)
cv.waitKey(0)