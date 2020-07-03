# -*- coding: utf-8 -*-

import cv2
import numpy as np

## BACKGROUND
width = int(input("Insert width: "))
height = int(input("Insert height: "))

img1 = cv2.imread('10 - messi5.jpg')
img2 = cv2.imread('10 - messi5.jpg')
###
#if img1.shape[1] > img1.shape[0]:
if width > height:
    scale_percent = width / img1.shape[1]
else:
    scale_percent = height / img1.shape[0]

dsize1 = (int(img1.shape[1]*scale_percent),int(img1.shape[0]*scale_percent))
img1 = cv2.resize(img1, dsize1)
##
img1width = img1.shape[1]
img1height = img1.shape[0]

##
px1 = int(img1width/2 - img1width/4)
px2 = int((img1width)/2 + (img1width)/4)
px3 = int(img1height/2 - img1height/4)
px4 = int((img1height)/2 + (img1height)/4)
##
dsize2 = (px2-px1,px4-px3)
img2 = cv2.resize(img2, dsize2)
##
img4 = np.copy(img1)
img4[px3:px4, px1:px2] = img2[0:px4-px3, 0:px2-px1]
##
cv2.imshow("img1",img4)


def mouse_event(event, x, y, flags, param):
    if event == cv2.EVENT_MOUSEMOVE:
        dsize2 = (x,y)
        img3 = cv2.resize(img2, dsize2)
        px1 = int(img1width/2 - x/2)
        px2 = int(img1width/2 + x/2)
        px3 = int(img1height/2 - y/2)
        px4 = int(img1height/2 + y/2)
        img4 = np.copy(img1)
        img4[px3:px4, px1:px2] = img3
        cv2.imshow("img1",img4)

cv2.setMouseCallback('img1',mouse_event)
cv2.waitKey(0)
cv2.destroyAllWindows()# -*- coding: utf-8 -*-

