from cv2 import cv2
import time

vid = cv2.VideoCapture(0)

a = 0 

while True:
    a = a+1
    check, frame = vid.read()

    print(check)
    print(frame)


    #time.sleep(20)
    cv2.imshow("Capturing", frame)
    key = cv2.waitKey(1)
    
    if key == ord('q'):
        break

print(a)
vid.release()
cv2.destroyAllWindows
