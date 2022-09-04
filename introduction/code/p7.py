import cv2 as cv
import numpy as np

img=cv.imread("rashi.jpg",cv.IMREAD_COLOR)

w,h,c=img.shape
print("No of channels in Image is ",c)
if img is None:
    print("Cannot Read the Image")

(B,G,R)=cv.split(img)


cv.imshow("Original Image",img)
cv.imshow("Blue channel",B)
cv.imshow("Green channel",G)
cv.imshow("Red channel",R)
cv.waitKey(0)