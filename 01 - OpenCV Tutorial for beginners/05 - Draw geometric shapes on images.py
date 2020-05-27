import numpy as np
import cv2

img = cv2.imread('samples/data/lena.jpg', 1)

img = cv2.line(img, (0,0), (255,500), (255,0,0), 10) # first point, end point, BGR COLOR CODE, thickness
img = cv2.arrowedLine(img, (365,0), (255,255), (50,90,0), 5)  # draw arrow
img = cv2.rectangle(img,(40,40),(80,80),(0,150,250), 2) # for a rectangle, a thickness of -1 will fill the area
img = cv2.circle(img,(400,400),50,(0,200,100), -1) # same for a circle. center point, radius, color, thiccness
font = cv2.FONT_HERSHEY_SIMPLEX #select a font to draw text
img = cv2.putText(img,'openCV', (10,500), font, 4, (255,105,255), 10, cv2.LINE_AA)

cv2.imshow('image',img)

k = cv2.waitKey(0)

if k == 27:
    cv2.destroyAllWindows() # close image if any key is pressed
elif k == ord('s'): # save new file when key S is pressed
    cv2.imwrite('05 - lena_geometric_shapes.png', img)
    cv2.destroyAllWindows()

### new drawings on a black image
img = np.zeros([512,512,3], np.uint8)
img = cv2.line(img, (68,255), (438,255), (255,0,0), 10) # first point, end point, BGR COLOR CODE, thickness
img = cv2.rectangle(img,(65,165),(440,250),(0,150,250), -1) # for a rectangle, a thickness of -1 will fill the area
img = cv2.arrowedLine(img, (0,225), (60,225), (120,90,120), 5)  # draw arrow
img = cv2.circle(img,(108,224),35,(120,60,120), -1) # same for a circle. center point, radius, color, thiccness
font = cv2.FONT_HERSHEY_SIMPLEX #select a font to draw text
img = cv2.putText(img,'openCV', (80,245), font, 3, (0,0,255), 8, cv2.LINE_AA)

cv2.imshow('black',img)

k = cv2.waitKey(0)

if k == 27:
    cv2.destroyAllWindows() # close image if ESCAPE key is pressed
elif k == ord('s'):
    cv2.imwrite('05 - black_geometric_shapes.png', img) # save new file when key S is pressed
    cv2.destroyAllWindows()