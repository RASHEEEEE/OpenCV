import numpy as np
import cv2 as cv

# Create a black image
img = np.zeros((400,400,3), np.uint8)
yvalue=10
for i in range(0,10):
    cv.line(img,(0,yvalue),(400,yvalue),(0,255,255),2)
    yvalue=yvalue+20
cv.imshow("Lines on Image",img)
cv.waitKey(0)