import cv2 as cv 
import numpy as np
img=np.zeros((400,400,3),np.uint8)
cv.circle(img,(200,200),40,(255,255,0),-1)
cv.circle(img,(100,100),20,(0,255,0),-1)
cv.circle(img,(300,300),20,(0,255,0),-1)
cv.imshow("circle in image",img)
cv.waitKey(0)
