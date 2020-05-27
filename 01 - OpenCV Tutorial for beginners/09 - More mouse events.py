import numpy as np
import cv2

def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        blue = img[y, x, 0]
        green = img[y, x, 1]
        red = img[y, x, 2]
        cv2.circle(img, (x,y), 3, (int(blue),int(green),int(red)), -1)
        pnts.append((x,y))
        if len(pnts) >= 2:
            cv2.line(img, pnts[-1], pnts[-2], (int(blue),int(green),int(red)), 3)
        cv2.imshow('image',img)

    if event == cv2.EVENT_MBUTTONDOWN: # show selected color in another window
        blue = img[y, x, 0]
        green = img[y, x, 1]
        red = img[y, x, 2]
        myColorImage = np.zeros((152,152,3), np.uint8) #black BGR image
        myColorImage[:] = [blue,green,red]
        cv2.imshow('color',myColorImage)
img = cv2.imread('03 - lena_copy.png')
cv2.imshow('image',img)
pnts = []

cv2.setMouseCallback('image',click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()