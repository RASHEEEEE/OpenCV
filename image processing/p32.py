import numpy as np
import cv2 as cv

img = cv.imread('noise4.png')
img_small=cv.resize(img,(400,400))
cv.imshow("Original Image",img_small)
kernel = np.ones((5,5),np.uint8)
opening = cv.morphologyEx(img_small, cv.MORPH_OPEN, kernel,iterations = 1)
cv.imshow("Opening Operation with kernel(5*5)",opening)
cv.waitKey(0)