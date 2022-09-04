import cv2 as cv 
import numpy as np 
img=np.zeros((500,1000,3),np.uint8)

text="To define is to limit"

cv.putText(img,text,(20,40),fontFace=cv.FONT_HERSHEY_DUPLEX,fontScale=1,color=(255,255,255))
cv.putText(img,text,(20,80),fontFace=cv.FONT_HERSHEY_SCRIPT_COMPLEX,fontScale=1,color=(255,255,255))
cv.imshow('Fonts', img) 
cv.waitKey(0)