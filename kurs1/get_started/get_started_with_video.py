import cv2 

# https://docs.opencv.org/3.4/dd/d43/tutorial_py_video_display.html

cap = cv2.VideoCapture(0) # захват видео
#cv2.VideoCapture("video.avi") или можно захватить видео фаил 

# Определите кодек и создайте объект VideoWriter
fourcc = cv2.VideoWriter_fourcc(*'XVID') # видео кодек 
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480)) # 20 - кол-во кадров и размер 

# бесконечно захватываем кадры с камеры если откры лась  пока пользователь не нажмет q 
while cap.isOpened():
  ret, frame = cap.read();   # читаю кадр ret - логическая переменная = true, если считался кадр

  if ret == True:
    # https://docs.opencv.org/4.0.0/d4/d15/group__videoio__flags__base.html#gaeb8dd9c89c10a5c63c139bf7c4f5704d
    cap.get() # можно получить и установить некоторые свойства видео 

    out.write(frame) # запись в файл

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # поменять цвет фрейма
    cv2.imshow('Video: ', frame) # воспроизвожу 

    if cv2.waitKey(1) == ord('q'): # Проверка на выход
      break
  else:
    break
cap.release()  # освобождает ресурсы
cv2.destroyAllWindows()
 