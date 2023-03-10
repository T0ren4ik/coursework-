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
    font = cv.FONT_HERSHEY_SIMPLEX
    
    if event == cv.EVENT_LBUTTONDOWN:
        print(f"{x} , {y}")
        strXY = str(x) + ", " + str(y)
        cv.putText(img, strXY, (x, y), font, .5 ,(255, 255, 0), 2)
        cv.imshow("image", img)
    elif event == cv.EVENT_RBUTTONDOWN:
        blue = img[y, x, 0]
        green = img[y, x, 1]
        red = img[y, x, 2]
        strBGR = f"{blue} , {green}, {red}"
        #strXY = str(blue) + ", " + str(green) + ", " + str(red)
        cv.putText(img, strBGR, (x, y), font, .5 ,(0, 255, 255 ), 2)
        cv.imshow("image", img)
      

#img = np.zeros((512, 512, 3), np.uint8)
img = cv.imread("get_started/lena.jpg")
cv.imshow("image", img)

cv.setMouseCallback("image", click_event)

cv.waitKey(0)
cv.destroyAllWindows()
