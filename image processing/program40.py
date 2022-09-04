import cv2
import matplotlib.pyplot as plt 

image = cv2.imread("gems.jpg")
img1= cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
# convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# create a binary thresholded image
ret, binary = cv2.threshold(gray, 225, 255, cv2.THRESH_BINARY_INV)

# show it
plt.imshow(binary, cmap="gray")
plt.show()
# find the contours from the thresholded image
contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# Find Number of contours
print("Number of Contours is: " + str(len(contours)))
# draw all contours
image = cv2.drawContours(img1, contours, -1, (0, 255, 0), 2)
# show the image with the drawn contours
plt.imshow(image)
plt.show()
