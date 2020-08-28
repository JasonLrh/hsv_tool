#!/usr/bin/env python3
import cv2 as cv
import numpy as np

img_name = './AB.jpg'
quick_config_file = './data.txt'

windowName = "pycv"
cv.namedWindow(windowName,cv.WINDOW_AUTOSIZE)
trackName = ['h','s','v','H','S','V']

def onChange(x):
    pass
cv.createTrackbar(trackName[0],windowName,0,180,onChange)
cv.createTrackbar(trackName[1],windowName,0,255,onChange)
cv.createTrackbar(trackName[2],windowName,0,255,onChange)
cv.createTrackbar(trackName[3],windowName,0,180,onChange)
cv.createTrackbar(trackName[4],windowName,0,255,onChange)
cv.createTrackbar(trackName[5],windowName,0,255,onChange)


img = cv.imread(img_name)
img = cv.resize(img,None,fx=0.1,fy=0.1,interpolation=cv.INTER_AREA)
hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)

colorpad=[0,0,0,0,0,0]

while(1):
    if quick_config_file is not None:
        with open(quick_config_file) as fil:
            line_num = 0
            for line in fil:
                wordlist = line.split()
                for a in wordlist:
                    number = int(a)
                    if colorpad[line_num] != number:
                        colorpad[line_num] = number
                        cv.setTrackbarPos(trackName[line_num],windowName,number)
                line_num += 1
    if hsv is None:
        break
    h=cv.getTrackbarPos('h',windowName)
    s=cv.getTrackbarPos('s',windowName)
    v=cv.getTrackbarPos('v',windowName)
    H=cv.getTrackbarPos('H',windowName)
    S=cv.getTrackbarPos('S',windowName)
    V=cv.getTrackbarPos('V',windowName)
    mask = cv.inRange(hsv,(h,s,v),(H,S,V))
    ( contours, hierarchy) = cv.findContours(mask,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_NONE)
    img_e = img.copy()
    img_e = cv.drawContours(img_e,contours,-1,(0,255,0),2)
    mask = cv.cvtColor(mask,cv.COLOR_GRAY2BGR)
    cv.imshow(windowName, np.hstack([img_e,mask]))
    key = cv.waitKey(1)
    if key > 0:
        break
cv.destroyAllWindows()