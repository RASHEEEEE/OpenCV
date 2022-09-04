import numpy as np
import cv2 as cv


# Create a black image
img = np.zeros((512,512,3), np.uint8)



# Draw a diagonal white line with thickness of 5 px
cv.line(img,(20,20),(400,100),(255,255,255),1)
cv.imshow("Image with Line",img)
cv.waitKey(0)