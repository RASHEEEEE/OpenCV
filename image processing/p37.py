
import cv2
from matplotlib import pyplot as plt


img=cv2.imread("rashi.jpg")
edges = cv2.Canny(img,200,300,10)
plt.figure()
plt.subplot(121)
plt.imshow(img,cmap = 'gray')
plt.title('Original Image')
plt.subplot(122)
plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image')
plt.show()