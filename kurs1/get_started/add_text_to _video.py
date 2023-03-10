import cv2 as cv 
import datetime as dt

cap = cv.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

while cap.isOpened():
    ret, frame = cap.read()

    if ret == True:
        
        font = cv.FONT_HERSHEY_SIMPLEX
        dateTime = "Time: " + str(dt.datetime.now()) 
        WidthHidth = "Width: " + str(cap.get(3)) + " Height: " + str(cap.get(4))
        frame = cv.putText(frame, dateTime, (10, 30), font, 1, (255, 255, 255), 2, cv.LINE_AA)
        frame = cv.putText(frame, WidthHidth, (10, 70), font, 1, (255, 255, 255), 2, cv.LINE_AA)

        cv.imshow('frame', frame)

        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
      break

cap.release() # освобождает ресурсы
cv.destroyAllWindows()
    