import cv2 as cv
import numpy as np

# посмотреть все ивенты
# функция dir() возвращает список имён, определяемых объектом
# events = [i for i in dir(cv) if 'EVENT' in i]
# print(events)

# https://docs.opencv.org/4.x/db/d5b/tutorial_py_mouse_handling.html

# эта функция будет срабатывать каждый раз когда будет происходить ивент мышью
# фиксация события и передача параметров происходит в функции setMouseCallback
# название окна должно быть одинаковым
def click_event(event, x, y, flags, param):
    if event == cv.EVENT_LBUTTONDOWN:
      cv.circle(img, (x, y), 3, (0, 0, 255), -1, cv.LINE_AA)
      points.append((x, y))
      if len(points) >= 2:
         cv.line(img, points[-2], points[-1], (255, 0, 0), 5)
      cv.imshow("image", img)
    elif event == cv. EVENT_RBUTTONDOWN:
       blue = img[x, y, 0]
       green = img[x, y, 1]
       red = img[x, y, 2]
       cv.circle(img, (x, y), 3, (0, 0, 255), -1, cv.LINE_AA)
       myColorImage = np.zeros((512, 512, 3), np.uint8)

       myColorImage[:] = [blue, green, red] # присвоение значений всем элементам
       cv.imshow("Color", myColorImage)
       cv.imshow("image", img)


#img = np.zeros((512, 512, 3), np.uint8)
img = cv.imread("get_started/lena.jpg")
points = []

cv.imshow("image", img)

cv.setMouseCallback("image", click_event)

cv.waitKey(0)
cv.destroyAllWindows()
