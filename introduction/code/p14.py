import cv2 as cv
import numpy as np

img1=cv.imread("G1.jpg",cv.IMREAD_COLOR)
img2=cv.imread("g2.jpg",cv.IMREAD_COLOR)
img1 = cv.resize(img1,(400,400))
img2 = cv.resize(img2,(400,400))
cv.imshow("Image 1",img1)
cv.imshow("Image 2",img2)

dst1 = cv.addWeighted(img1, 0.7, img2, 0.3, 0.0)
cv.imshow("Blended Image1",dst1)
cv.waitKey(0)