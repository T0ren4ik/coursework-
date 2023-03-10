import cv2 as cv
import numpy as np 

# https://docs.opencv.org/4.x/d3/df2/tutorial_py_basic_ops.html

img = cv.imread("get_started/messi5.jpg")
img2 = cv.imread("get_started/opencv-logo.png")

print(img.shape) # вернет картеж c числоv строк, столбцов и каналов
print(img.size)  # вернет итоговое число пикселей
print(img.dtype) # верент тип данных изображения uint8
b,g,r = cv.split(img) # разделение на bgr в однаканальные массивы
img = cv.merge((b,g,r)) # обьединение одноканальных в многоканальный

# можем вырезать изобращение c картинки
ball = img[280:340, 330:390]
# b поместить в другие координаты
img[273:333, 100:160] = ball

# для смешивания двух картинок нужан один размер 
img = cv.resize(img, (512, 512))
img2 = cv.resize(img2, (512, 512))
dst = cv.add(img, img2) # мешаем

# можем мешать с весом
dst2 = cv.addWeighted(img, .5, img2, .5, 0)
 
cv.imshow("addimage", dst)
cv.imshow("addWeightedimage", dst2)
cv.waitKey(0)
cv.destroyAllWindows()
