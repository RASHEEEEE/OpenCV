import cv2 as cv
# Load two images
water = cv.imread('g2.jpg')
fish = cv.imread('zeb.jpg')
waterimg=cv.resize(water,(300,300))
fishimg=cv.resize(fish,(300,300))
cv.imshow("sky Image",waterimg)
cv.imshow("lady Image",fishimg)

cv.waitKey(0)
cv.destroyAllWindows()

# I want to put lady image on top-left corner, So I create a ROI
rows,cols,channels = fishimg.shape
roi = waterimg[0:rows, 0:cols] #selecting the portion/region of water image which has same size as fish image
# Now create a mask of fish and create its inverse mask also
cv.imshow("Region of Interest ", roi)
fishimggray = cv.cvtColor(fishimg,cv.COLOR_BGR2GRAY)
ret, mask = cv.threshold(fishimggray, 20, 255, cv.THRESH_BINARY)
mask_inv = cv.bitwise_not(mask)
cv.imshow("Mask",mask)
cv.imshow("Inverse Mask",mask_inv)
cv.waitKey(0)
cv.destroyAllWindows()
# Now black-out the area of fish in ROI
waterimg_bg = cv.bitwise_and(roi,roi,mask = mask_inv)
cv.imshow("sky Image Background",waterimg_bg)
# Take only region of fish from fish image.
fishimg_fg = cv.bitwise_and(fishimg,fishimg,mask = mask)
# Put fish in ROI and modify the main image
cv.imshow("lady Image Foreground",fishimg_fg)
dst = cv.add(waterimg_bg,fishimg_fg)
waterimg[0:rows, 0:cols ] = dst
cv.imshow('res',waterimg)
cv.waitKey(0)
cv.destroyAllWindows()