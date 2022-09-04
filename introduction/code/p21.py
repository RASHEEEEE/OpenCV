import numpy as np
import cv2 as cv

img=cv.imread("20image.png",cv.IMREAD_COLOR)
cv.imshow("Original Image",img)
img_1=cv.resize(img,(400,400),interpolation=cv.INTER_NEAREST)
cv.imshow("Nearest neighbour interpolation",img_1)
img_2=cv.resize(img,(400,400),interpolation=cv.INTER_LINEAR)
cv.imshow("Linear interpolation",img_2)
img_3=cv.resize(img,(400,400),interpolation=cv.INTER_AREA)
cv.imshow("AREA interpolation",img_3)
img_4=cv.resize(img,(400,400),interpolation=cv.INTER_CUBIC)
cv.imshow("Cubic interpolation",img_4)
cv.waitKey(0)