import cv2 as cv
import numpy as np

# read the image
img1 = np.zeros((250, 500, 3), np.uint8)
img1 = cv.rectangle(img1, (200, 0), (300, 100), (255, 255, 255), -1)
img2 = cv.imread('get_started/image_1.png')

# работает как логическое операция умножения 
bitAdn = cv.bitwise_and(img2, img1)
bitOr = cv.bitwise_or(img2, img1)
bitXor = cv.bitwise_xor(img2, img1)
bitNot = cv.bitwise_not(img2)

cv.imshow('img1', img1)
cv.imshow('img2', img2)
cv.imshow('bitAdn', bitAdn)
cv.imshow('bitOr', bitOr)
cv.imshow('bitXor', bitXor)
cv.imshow('bitNot', bitNot)

cv.waitKey(10000)
cv.destroyAllWindows()
