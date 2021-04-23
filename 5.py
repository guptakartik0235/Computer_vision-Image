import cv2
c = (str(input("You want Image to be Canny :- ")).lower())



path = "Ai_Practical\images\lambo.jpg"

if c == "y":
    Image = cv2.imread(path)
    Image_C = cv2.Canny(Image,10,10)
    
    cv2.imshow("2nd",Image_C)
    cv2.waitKey(0)
else : 
    g = (str(input("You Want Image to be Grayscale :- ")).lower())
    if g =='y':
        #Reading Image
        Image = cv2.imread(path)

#Converting Image
        Image_BW = cv2.cvtColor(Image,cv2.COLOR_BGR2GRAY)

#Displaying Image

        cv2.imshow("2nd",Image_BW)
        cv2.waitKey(0)
    else:
        v = (str(input("You want to play Video :- ")).lower())
        if v == "y":
                video = cv2.VideoCapture(path)

#Video reading
                while True :
                    success , img =  video.read()
                    cv2.imshow("Video",img)

#The Program fires when 'q' key is pressed
                    if cv2.waitKey(1) & 0xFF ==ord('q'):
                        break
        else:
            print("You selected No Option")


#Stopping from closing
    

