import cv2 as cv
import numpy as np

def nothing(x):
    print(x)

# create a black image 300 in 512 px, a window
img = np.zeros((300, 512, 3), np.uint8)
cv.namedWindow('image')

# создаем трэкбар, который дает возможность выбрать хначение
cv.createTrackbar('B', 'image', 0, 255, nothing)
cv.createTrackbar('G', 'image', 0, 255, nothing)
cv.createTrackbar('R', 'image', 0, 255, nothing)

sw = '0 : OFF\n 1 : ON'
cv.createTrackbar(sw, 'image', 0, 1, nothing)

while True:
    cv.imshow('image', img)
    key = cv.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    
    # принимает заданное значение из трэкбара 
    b = cv.getTrackbarPos('B', 'image')
    g = cv.getTrackbarPos('G', 'image')
    r = cv.getTrackbarPos('R', 'image')
    s = cv.getTrackbarPos(sw, 'image')

    if s == 1:
      img[:] = [b, g, r]
    else:
      img[:] = 0

cv.destroyAllWindows()
