import numpy as np
import cv2 as cv
img1=cv.imread("rashi.jpg",cv.IMREAD_COLOR)
img=cv.resize(img1,(300,300))
cv.imshow("Original Image",img)
hsvImage = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow("HSV Image",hsvImage)
cv.waitKey(0)
print("The pixel Value at 100,10 is ",hsvImage[100,10])