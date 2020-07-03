import cv2
import numpy as np

width = int(input("Insert width: "))
height = int(input("Insert height: "))

#img1 = np.zeros((height,width,3),np.uint8)
img1 = cv2.imread('10 - messi5.jpg')
img2 = cv2.imread('10 - messi5.jpg')
#
dsize1 = (width,height)
img1 = cv2.resize(img1, dsize1)
#
img1width = img1.shape[1]
img1height = img1.shape[0]
#
px1 = int(img1width/2 - img1width/4)
px2 = int((img1width)/2 + (img1width)/4)
px3 = int(img1height/2 - img1height/4)
px4 = int((img1height)/2 + (img1height)/4)
#
dsize2 = (px2-px1,px4-px3)
img2 = cv2.resize(img2, dsize2)
#
img1[px3:px4, px1:px2] = img2[0:px4-px3, 0:px2-px1]
#
cv2.imshow("img1",img1)
cv2.waitKey(0)
cv2.destroyAllWindows()