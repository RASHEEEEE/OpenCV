from matplotlib import pyplot as plt
import numpy as np
import cv2 as cv

img=cv.imread("rori.jpg")
cv.imshow("Original Image ", img)
h,w,c=img.shape

mask = np.zeros(img.shape[:2], dtype="uint8")
cv.rectangle(mask, (60, 60), (210, 250), 255, -1)
cv.imshow("Mask", mask)

masked = cv.bitwise_and(img, img, mask=mask)
cv.imshow("Applying the Mask", masked )
color = ('b','g','r')

plt.figure(figsize=(8,8))
plt.subplot(211)

plt.title("Original Image Histogram")
for i,col in enumerate(color):
    histr = cv.calcHist([img],[i],None,[256],[0,256])
    plt.plot(histr,color = col)
    plt.xlim([0,256])
plt.subplot(212)
plt.title("Histogram of Masked Image")
for i,col in enumerate(color):
    histr = cv.calcHist([img],[i],mask,[256],[0,256])
    plt.plot(histr,color = col)
    plt.xlim([0,256])
plt.show()
cv.waitKey(0)
