import numpy as np
import cv2 as cv

img1=cv.imread("sunflower.jpg",cv.IMREAD_COLOR)
img=cv.resize(img1,(400,400))
cv.imshow("Original Image",img)
hsvImage = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow("HSV Image",hsvImage)

low_b = np.array([160,100,100])
high_b = np.array([179,255,255])

low_y = np.array([22, 100, 100])
high_y = np.array([38,255,255])

mask1 = cv.inRange(hsvImage, low_b, high_b)

mask2=cv.inRange(hsvImage,low_y,high_y)
cv.imshow("Mask2",mask2)
final_mask=mask1+mask2
cv.imshow("Final mask",final_mask)
outputimg=cv.bitwise_and(img,img,mask=final_mask)
cv.imshow("Output Image",outputimg)
cv.waitKey(0)
