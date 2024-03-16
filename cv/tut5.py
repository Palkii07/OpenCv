# colors
#bgr->hsv color scheme
import numpy as np
import cv2
cap=cv2.VideoCapture(0) #no of webcams () ->  or ('') link of video
while True:
    ret,frame=cap.read()
    width=int(cap.get(3))
    height=int(cap.get(4))
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    lower_pink = np.array([140, 50, 50])  # Lower bound for pink
    upper_pink = np.array([170, 255, 255]) 
    mask=cv2.inRange(hsv,lower_pink,upper_pink)
    res=cv2.bitwise_and(frame,frame,mask=mask)
    
    cv2.imshow('frame',res)
    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()



#  to convert 1 indiv pixel to hsv
# val = np.array([[[181,45,180]]], dtype=np.uint8)  # Specify dtype as np.uint8
# x = cv2.cvtColor(val, cv2.COLOR_BGR2HSV)
# print(x)
# # pink->163,192,181
# # 150,192,181