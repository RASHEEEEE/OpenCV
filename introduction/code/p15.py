import numpy as np
import cv2 as cv

img1=np.zeros((400,400,3),np.uint8)
cv.rectangle(img1,(20,20),(100,150),(0,0,255),-1)
img2=np.zeros((400,400,3),np.uint8)
cv.rectangle(img2,(40,40),(100,150),(255,0,0),-1)
cv.imshow("Image 1",img1)
cv.imshow("Image 2",img2)
dst1=cv.bitwise_and(img1,img2)
cv.imshow("Bitwise AND Operation",dst1)
dst2=cv.bitwise_or(img1,img2)
cv.imshow("Bitwise OR Operation",dst2)
dst3=cv.bitwise_xor(img1,img2)
cv.imshow("Bitwise XOR Operation",dst3)
dst4=cv.bitwise_not(img1)
cv.imshow("Bitwise NOT Operation",dst4)
cv.waitKey(0)