# -*- coding: utf-8 -*-
import cv2
import numpy as np
def nothing(x):
    pass

mousePosX = 0
mousePosY = 0
mouseClick = ()
mouseRelease = ()
leftClick = False

def mouse_event(event, x, y, flags, param):
    global mousePos, mouseClick, mouseRelease, leftClick
    
    if event == cv2.EVENT_MOUSEMOVE:
#        mousePosX = x
        mousePosY = y
#        print('(' + str(x) + ',' + str(y) + ')')
    if event == cv2.EVENT_LBUTTONDOWN:
#        mouseClick = (x,y)
        leftClick = True
#        print('leftClick = ' + str(leftClick) + ' at (' + str(x) + ',' + str(y) + ')')

    if event == cv2.EVENT_LBUTTONUP:
#        mouseRelease = (x,y)
        leftClick = False
#        print('leftClick = ' + str(leftClick) + ' at (' + str(x) + ',' + str(y) + ')')



cv2.namedWindow('image')
img = cv2.imread('10 - messi5.jpg')  
b,g,r = cv2.split(img)
img_copy = np.copy(img)

cv2.createTrackbar('B','image',0,600,nothing)
cv2.createTrackbar('G','image',0,600,nothing)
cv2.createTrackbar('R','image',0,600,nothing)

while(1):
    b_pos = cv2.getTrackbarPos('B','image')
    g_pos = cv2.getTrackbarPos('G','image')
    r_pos = cv2.getTrackbarPos('R','image')
#    b_pos = 1
    b_copy = np.divide(b,b_pos)
    b_copy = np.round(b_copy,0)
    g_copy = np.divide(g,g_pos)
    g_copy = np.round(g_copy,0)
    r_copy = np.divide(r,r_pos)
    r_copy = np.round(r_copy,0)
    img_copy = cv2.merge((b_copy,g_copy,r_copy))
#    img_copy = b_copy
    cv2.imshow('image',img_copy)
    cv2.setMouseCallback('image',mouse_event)
    
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
    

cv2.destroyAllWindows()# -*- coding: utf-8 -*-