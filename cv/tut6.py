# cornor detection
# shi tomasi cornor algo
import numpy as np
import cv2
# works on grayscale image
img=cv2.imread('assets/chessboard.png')
img=cv2.resize(img,(0,0),fx=0.75,fy=0.75)
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

cornor=cv2.goodFeaturesToTrack(gray,100,0.5,10)
cornor=np.int0(cornor)
for c in cornor:
    x,y=c.ravel() #flatten an arrys
    cv2.circle(img,(x,y),5,(255,0,0),-1)
for i in range(len(cornor)):
    for j in range(i+1,len(cornor)):
        corner1=tuple(cornor[i][0])
        corner2=tuple(cornor[j][0])
        color=tuple(map(lambda x:int(x),np.random.randint(0,255,size=3)))#numpy->32 bit or 64 bit integer,we want 8 bit int
        cv2.line(img,corner1,corner2,(color),1)
cv2.imshow('frame',img)
cv2.waitKey(0)
cv2.destroyAllWindows()