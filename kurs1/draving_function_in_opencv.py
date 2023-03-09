import numpy as np
import cv2 as cv

img = cv.imread('lesson_3/lena.jpg', 0)

cv.imshow('image', img)

cv.waitKey(0)
cv.destroyAllWindows()
