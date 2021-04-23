#Imported Library
import cv2
import numpy as np
#added path
path = "Ai_Practical\images\lambo.jpg"

#Reading Image

Image = cv2.imread(path)
Image_C = cv2.Canny(Image,10,10)
Image_BW = cv2.cvtColor(Image,cv2.COLOR_BGR2GRAY)

#Displaying Image
Img = np.vstack((Image_BW,Image_C))
cv2.imshow("stacked",Img)
#Stopping from closing
cv2.waitKey(0)