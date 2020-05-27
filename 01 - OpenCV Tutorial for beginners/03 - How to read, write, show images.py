import cv2

img = cv2.imread('samples/data/lena.jpg', 1) # read image

print(img) # print in console

cv2.imshow('image',img) # show image

k = cv2.waitKey(0) # prevent closing window

if k == 27:
    cv2.destroyAllWindows() # close image if ESCAPE key is pressed
elif k == ord('s'):
    cv2.imwrite('03 - lena_copy.png', img) # save new file when key S is pressed
    cv2.destroyAllWindows()
