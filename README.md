# Computer_vision-Image

## Introduction
Hey! I am Kartik Gupta.<br />
I have made this repository about using basic features of [Computer Vision](https://en.wikipedia.org/wiki/Computer_vision) Library.

***

## Requirments
* Any IDE ([VS Code](https://code.visualstudio.com/download) or [Pycharm](https://www.jetbrains.com/pycharm/download)) for running Python
* Python version [3.6.0](https://www.python.org/downloads/) or higher
* [Cv2](https://pypi.org/project/opencv-python/) & [Numpy](https://numpy.org/install/) modules to be installed.

***

## **Codes**
1. [Canny Image](https://github.com/guptakartik0235/Computer_vision-Image/blob/main/README.md#1st-code)
2. [Grayscale Image](https://github.com/guptakartik0235/Computer_vision-Image/blob/main/README.md#2nd-code)
3. [HSV Image](https://github.com/guptakartik0235/Computer_vision-Image/blob/main/README.md#3rd-code)
4. [Video or Webcam](https://github.com/guptakartik0235/Computer_vision-Image/blob/main/README.md#4th-code)
5. [All Type Image](https://github.com/guptakartik0235/Computer_vision-Image/blob/main/README.md#5th-code)
6. [Stacking Images](https://github.com/guptakartik0235/Computer_vision-Image/blob/main/README.md#7th-code)

***

## **Explanation**
***
* ### __[1st Code](1.py)__ ###

**Inputs** - The code requires the path within double inverted commas to be changed by path of any Image.

**Working** - The code uses [Canny](https://docs.opencv.org/master/da/d22/tutorial_py_canny.html) function of opencv library to find Edges of a particular Image.

**Results** - It displays Edges of the Given Images & print an Image with Edges.

**Applications** - It is used in various Shapedetector Projects to count the Edges.

**The Output is as shown below** <br />
![1st code img](https://user-images.githubusercontent.com/81790487/115868157-a3146700-a459-11eb-9e4f-dc1ee64f28d2.PNG)

***
* ### __[2nd Code](2.py)__ ###

**Inputs** - The code requires the path within double inverted commas to be changed by path of any Image.

**Working** - The code uses cvt color function of cv2 library to convert color of Image to Grayscale.

**Results** - It displays the RGB image you provided in Grayscale format.

**Applications** - It is used while making various projects based on Computer Vision .

**The Output is as shown below** <br />
![2nd code img](https://user-images.githubusercontent.com/81790487/115870522-fb993380-a45c-11eb-905c-fc853d5643da.PNG)


***

* ### __[3rd Code](3.py)__ ###
**Inputs** - The code requires the path within double inverted commas to be changed by path of any Image.

**Working** - The code uses cvt color & BGR2HSV function of opencv library to convert Image to HSV Image.

**Results** - It displays Image according to Hue, Saturation & value of Lightness of Image.

**Applications** - It is used in various Color Detection Opencv Programs.

**The Output is as shown below** <br />
![3rd img code](https://user-images.githubusercontent.com/81790487/115872143-15d41100-a45f-11eb-8cfb-818c0d4c57d8.PNG)

***

* ### __[4th Code](4.py)__ ###

**Inputs** - The code requires the path within double inverted commas to be changed by path of any Video or just simply type 0 without commas for Webcam.

**Working** - The code uses video Capture function of cv2 & uses while loop to make the video run constantly .

**Results** - It displays Video or Webcam according to the path provided by you.

**Applications** - It is used in realtime detection Programs for webcams.

**The Output is as shown below** <br />


***
* ### __[5th Code](5.py)__ ###

**Inputs** - The code requires the input as Y or N if u want to display the type of image or Video .It also requires path to be changed to image that is to be shown.

**Working** - The code uses various elif conditions to display image you selected .

**Results** - It displays the type of Image you selected to display.

**The Output is as shown below** <br />
![5th code img](https://user-images.githubusercontent.com/81790487/115878897-b7129580-a466-11eb-8f16-f66ba8b5b1ee.PNG)

***

* ### __[6th Code](6.py)__ ###

**Inputs** - It requires the path in the code to be changed to any Image you want .

**Working** - The code uses stacking function of numpy to stack our images together  .

**Results** - It displays the Grayscale & Canny image of selected Image & stack them together  .

**Applications** - It is used for make our output look in a formal & standard manner.

**The Output is as shown below** <br />

![6th code img](https://user-images.githubusercontent.com/81790487/115879842-baf2e780-a467-11eb-8b17-926017f61dff.PNG)




