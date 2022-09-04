import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml') #Load the cascade
img = cv2.imread('faces6.jpg')
img=cv2.resize(img,(400,200)) #Read the input image
cv2.imshow("Multiple Face image",img)

faces = face_cascade.detectMultiScale(img,1.1 ,12) #Detect faces
#Draw rectangle around the faces
for (x, y, w, h) in faces:
 cv2.rectangle(img, (x, y), (x+w, y+h), (255, 255, 255), 2)
#Export the result
cv2.imwrite("face_detected.jpg", img)
detected = cv2.imread("face_detected.jpg",cv2.IMREAD_COLOR)
cv2.imshow("Detected Face", detected)
cv2.waitKey(0)
print('Photo successfully exported!')