import cv2 as cv 
import numpy as np

img1=cv.imread("sky.jpg",cv.IMREAD_COLOR)
img2=cv.imread("rainbow.jpg",cv.IMREAD_COLOR)
img1 = cv.resize(img1,(450,300))
img2 = cv.resize(img2,(450,300))
cv.imshow("Image 1",img1)
cv.imshow("Image 2",img2)

dst1 = cv.addWeighted(img1, 0.5, img2, 0.3, 0.0)
cv.imshow("Blended Image",dst1)
cv.waitKey(0)