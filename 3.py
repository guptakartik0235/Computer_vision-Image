#Imported Library
import cv2

#added path
path = "Ai_Practical\images\lambo.jpg"

#Reading Image
Image = cv2.imread(path)

#Converting Image
Image_Hsv = cv2.cvtColor(Image,cv2.COLOR_BGR2HSV)

#Displaying Image
cv2.imshow("1st",Image)
cv2.imshow("2nd",Image_Hsv)

#Stopping from closing
cv2.waitKey(0)