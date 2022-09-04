import cv2 as cv
import numpy as np

img=cv.imread("rashi.jpg",cv.IMREAD_COLOR) # img is cv::mat object
if img is None:
    print("Cannot read the image")


px = img[400,600] #returns the list which contains B,G,R intensity
print(px)
print("The intensity of Blue color is",px[0])
print("The intensity of Green color is",px[1])
print("The intensity of Red color is",px[2])


print("Modifying pixel value at co-ordinate(100,10)")
img[100,10]=[255,255,255] # white color
cv.imshow("Modified Image 1",img)
cv.waitKey(0)


print("Modifying a patch of Image with red color")
img[20:300,20:150]=[0,255,255]
cv.imshow("Modified Image 2",img)
cv.waitKey(0)