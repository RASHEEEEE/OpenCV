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


h,w,c=frame.shape
cx,cy=(w/2,h/2)
M1 = cv.getRotationMatrix2D((cx, cy), 45, 1.0)
print(M1)
rotated1 = cv.warpAffine(frame, M1,(w,h))
cv.imshow("Rotated by 45 Degrees", rotated1)
cv.waitKey(0)
cap.release()
out.release()
cv.destroyAllWindows()