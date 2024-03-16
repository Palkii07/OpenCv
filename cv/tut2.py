import cv2
# (rows,col,channnels)
import random
img=cv2.imread('assets/vk.jpg',-1)
# **********to manipulate an image************
# for i in range(100):
#     for j in range(img.shape[1]):
#         img[i][j]= [random.randint(0,255),random.randint(0,255),random.randint(0,255)]

# copy and paste in an image****
# tag=img[100:130,100:130]   # has to be same shape neeche
# img[90:120,90:120]=tag       # copying tag into the main image

print(img)


# cv2.imshow('Image',img) 
# cv2.waitKey(0)
# cv2.destroyAllWindows()

