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
        mousePosX = x
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

cv2.createTrackbar('threshold_B','image',0,300,nothing)
cv2.createTrackbar('max_binary_B','image',0,300,nothing)
cv2.createTrackbar('threshold_G','image',0,300,nothing)
cv2.createTrackbar('max_binary_G','image',0,300,nothing)
cv2.createTrackbar('threshold_R','image',0,300,nothing)
cv2.createTrackbar('max_binary_R','image',0,300,nothing)
cv2.createTrackbar('threshold_algorithm','image',0,4,nothing)

while(1):
    threshold_B = cv2.getTrackbarPos('threshold_B','image')
    max_binary_B = cv2.getTrackbarPos('max_binary_B','image')
    threshold_G = cv2.getTrackbarPos('threshold_G','image')
    max_binary_G = cv2.getTrackbarPos('max_binary_G','image')
    threshold_R = cv2.getTrackbarPos('threshold_R','image')
    max_binary_R = cv2.getTrackbarPos('max_binary_R','image')
    thresh_algorithm = cv2.getTrackbarPos('threshold_algorithm','image')
    if thresh_algorithm == 0:
        thrAlg = cv2.THRESH_BINARY
    elif thresh_algorithm == 1:
        thrAlg = cv2.THRESH_BINARY_INV
    elif thresh_algorithm == 2:
        thrAlg = cv2.THRESH_TRUNC
    elif thresh_algorithm == 3:
        thrAlg = cv2.THRESH_TOZERO
    else:
        thrAlg = cv2.THRESH_TOZERO_INV
        
    b_copy = np.copy(b)
    g_copy = np.copy(g)
    r_copy = np.copy(r)
    
    _,b_copy = cv2.threshold(b_copy, threshold_B, max_binary_B, thrAlg  )
    _,g_copy = cv2.threshold(g_copy, threshold_G, max_binary_G, thrAlg  )
    _,r_copy = cv2.threshold(r_copy, threshold_R, max_binary_R, thrAlg  )
    
    img_copy = cv2.merge((b_copy,g_copy,r_copy))
    
    cv2.imshow('image',img_copy)
    cv2.setMouseCallback('image',mouse_event)
    
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
    

cv2.destroyAllWindows()# -*- coding: utf-8 -*-# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-

