import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('hist1.jpg',cv.IMREAD_GRAYSCALE)
gray_image=cv.resize(img,(400,400))
cv.imshow("GRAY Scale Image",gray_image)

hist = cv.calcHist([gray_image], [0], None, [256], [0, 256])
plt.figure()
plt.title("Grayscale Histogram")
plt.xlabel("Intensity")
plt.ylabel("# of Pixels")
plt.plot(hist)
plt.xlim([0,256])
plt.show()