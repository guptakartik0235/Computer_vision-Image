#Importing Library
import cv2

#Opening Webcam
video = cv2.VideoCapture(0)

#Video reading
while True :
    success , img =  video.read()
    cv2.imshow("Video",img)

#The Program fires when 'q' key is pressed
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break
