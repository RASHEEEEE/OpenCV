import cv2 as cv
import numpy as np

img = cv.imread("rose.jpg") #img is cv::mat object
image =cv.resize(img,(400,400))
# Convert BGR to HSV
hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)
cv.imshow("Original Image and HSV Image",np.hstack((image,hsv)))
# define blue color
low_b = np.array([160,100,100])
high_b = np.array([179,255,255])
#define yellow color
low_y = np.array([22, 100, 100])
high_y = np.array([38,255,255])
# Threshold the HSV image to get only blue and yellow colors
mask1 = cv.inRange(hsv, low_b, high_b)
cv.imshow("Mask1",mask1)
mask2=cv.inRange(hsv,low_y,high_y)
cv.imshow("Mask2",mask2)
final_mask=mask1+mask2
cv.imshow("Final mask",final_mask)
outputimg=cv.bitwise_and(image,image,mask=final_mask)
cv.imshow("Output Image",outputimg)
cv.waitKey(0)
