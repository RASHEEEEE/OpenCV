import numpy as np
import cv2 as cv
cap = cv.VideoCapture(0) 
frame_width = int(cap.get(cv.CAP_PROP_FRAME_WIDTH)) 
frame_height = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))

fourcc = cv.VideoWriter_fourcc(*'XVID')

out = cv.VideoWriter('output.avi', fourcc, 24.0, (frame_width, frame_height))
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    out.write(frame)
    cv.imshow('frame', frame)
    if cv.waitKey(1) == ord('q'):
        break

cap.release()
out.release()
cv.destroyAllWindows()