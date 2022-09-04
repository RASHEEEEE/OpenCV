import cv2 as cv
import numpy as np

img1=np.full((400,400,3),(100,5,56),np.uint8)
img2=np.full((400,400,3),(67,34,90),np.uint8)

cv.imshow("Image1",img1)
cv.imshow("Image2",img2)

img= cv.add(img1,img2)
print("Pixel Value at Location(200,200)",img[200,200])
cv.imshow("Added Image",img)
cv.waitKey(0)