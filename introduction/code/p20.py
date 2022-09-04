import numpy as np
import cv2 as cv

img = cv.imread('rose.jpg', 1)
cv.imshow('Original Image', img)
#To downscale the image to half size, we can pass the fx and fy value to 0.5.
img_half = cv.resize(img,(0,0),fx=0.5, fy=0.5)
cv.imshow('Half Size Image', img_half)
#To upscale the image to double size, we can pass the fx and fy value to 2.0
img_double= cv.resize(img,(0,0),fx=2.0,fy=2.0)
cv.imshow("Double size Image",img_double)
# Scaling image to fixed size
# Here the image is set to have width is 400 and height is 1000
img_fixed=cv.resize(img,(400,1000))
cv.imshow("Fixed Size Image",img_fixed)
cv.waitKey(0)
cv.destroyAllWindows()