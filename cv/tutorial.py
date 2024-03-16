import cv2
# to load  RGB-> BGR
#load in coloured,gray,or transparency
#-1,cv2.IMREAD_COLOR: Loads a color  image. It is the default flag.
#0,cv2.IMREAD_UNCHANGED: Loads an image as it is (with alpha channel). The loaded image will have the alpha channel if it has one; otherwise
# 1,cv2.IMREAD_GRAYSCAle

img=cv2.imread('assets/vk.jpg',0)
# img=cv2.resize(img,(400,400))
img=cv2.resize(img,(0,0),fx=2,fy=2)
img=cv2.rotate(img,cv2.ROTATE_90_COUNTERCLOCKWISE)
# TO SAVE
cv2.imwrite('new_image.jpg',img)
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()