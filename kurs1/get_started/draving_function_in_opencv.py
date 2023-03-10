import numpy as np
import cv2 as cv

# https://docs.opencv.org/4.x/dc/da5/tutorial_py_drawing_functions.html

img = cv.imread('get_started/lena.jpg', 0)
# можем создать изображение с помощью np 
# это изображение размером 255x255 с 3 каналами
# img = np.zeros([512,512, 3])

# нарисовали ринию на img c двумя координатами и цветом, а также ширину 5 px
img = cv.line(img, (0,0), (255, 255), (255, 0, 0), 5)
# рисуем стрелку
img = cv.arrowedLine(img, (0,255), (255, 255), (0, 0, 255), 10)
# рисуем квадрат закрашенный
img = cv.rectangle(img, (384, 0), (510, 128), (10, 255, 12), -2)
# закраашенную окружность 
img = cv.circle(img, (447, 63), 63, (255, 255,255), -1)
# пишем 
fontfase = cv.FONT_HERSHEY_SIMPLEX
img = cv.putText(img, "OpenCv", (10, 500), fontfase, 4, (255, 255, 255), 5, cv.LINE_AA)

cv.imshow('image', img)

cv.waitKey(0)
cv.destroyAllWindows()
