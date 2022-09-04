import numpy as np
import cv2

my_img  = np.zeros((512, 612, 3), dtype = "uint8")

list_of_points=[50,75,100,125,150]
colors = [[239,70,104], [87,239,70], [0,0,255], [0,255,239], [255,255,255]]


for i in range(0,len(colors)):
    start = list_of_points[i]+50
    clr = tuple(colors[i])
    my_img = cv2.rectangle(my_img, (start,start), (start+200,start+200), clr, 10)
    my_img = cv2.rectangle(my_img, (start,start), (start+200,start+200), (0,0,0), -1)
    
cv2.imshow('My Image', my_img)
cv2.waitKey(0)
cv2.destroyAllWindows()