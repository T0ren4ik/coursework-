import cv2

# чтение изображения как массив
# cv2.IMREAD_GRAYSCALE = 0  В оттенках серого  
# cv2.IMREAD_UNCHANGED = -1 В альфа канале
# cv2.IMREAD_COLOR = 1      Цветное изображение
img_array = cv2.imread("lesson_3\lena.jpg", 1)   

# Визуализация
cv2.imshow('image', img_array) 
key = cv2.waitKey(0) # ждать нажатия кнопки 

if key == 27: # кдлавиша Esc
  cv2.destroyAllWindows()
elif key == ord('s'):
  # Запись изображения в фаил
  cv2.imwrite('lesson_3\lena_copy.png', img_array) 
  cv2.destroyAllWindows()
else:
  cv2.destroyAllWindows()