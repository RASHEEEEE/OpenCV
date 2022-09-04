import cv2 as cv
import numpy as np

img = cv.imread('binary.png')
img_small=cv.resize(img,(400,400))
cv.imshow("Original Image",img_small)

kernel = np.ones((5,5),np.uint8)
dilation = cv.dilate(img_small,kernel,iterations = 3)
cv.imshow("The Dilated image with kernel(5*5)",dilation)
cv.waitKey(0)