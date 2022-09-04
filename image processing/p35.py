import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt


image=cv.imread("rashi.jpg",cv.IMREAD_COLOR)
img = cv.cvtColor(image, cv.COLOR_BGR2RGB)

hist1 = cv.calcHist([img],[0],None,[256],[0,256]) # for blue channel
hist2 = cv.calcHist([img],[1],None,[256],[0,256]) # for green channel
hist3 = cv.calcHist([img],[2],None,[256],[0,256]) # for red channel
plt.figure(figsize=(10,10))
plt.title("Histogram for Blue, Green, Red Channels of Image")
plt.subplot(221)
plt.title("Original Image")
plt.imshow(img)
plt.subplot(222)
plt.title("Blue Channel Histogram")
plt.plot(hist1,color='b')
plt.subplot(223)
plt.title("Greeen Channel Histogram")
plt.plot(hist2,color='g')
plt.subplot(224)
plt.title("Red Channel Histogram")
plt.plot(hist3,color='r')
plt.xlim([0,256])
plt.show()