import cv2 as cv 
import numpy as np

img=np.zeros((400,400,3),np.uint8)

cv.line(img, (20, 160), (100, 160), (0, 0, 255), 10)
cv.rectangle(img,(10,10),(200,300),(0,255,255),3)
cv.rectangle(img,(20,20),(100,150),(255,0,0),-1)
cv.rectangle(img,(40,40),(100,150),(255,0,255),-1)
cv.imshow("solid and hollow rectangle in image",img)
cv.waitKey(0)