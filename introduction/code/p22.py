import numpy as np
import cv2 as cv

img=cv.imread("rose.jpg",cv.IMREAD_COLOR)
cv.imshow("Original Image",img)
rows,cols,c = img.shape
print("Rows and Cols :",rows,cols,c)
M1 = np.float32([[1,0,100],[0,1,50]])
dst1 = cv.warpAffine(img,M1,(cols,rows))
cv.imshow("Translated Image 100 pixels right,50 pixels down",dst1)
M2 = np.float32([[1,0,-100],[0,1,-50]])
dst2 = cv.warpAffine(img,M2,(cols,rows))
cv.imshow("Translated Image 100 pixels left,50 pixels up",dst2)
cv.waitKey(0)