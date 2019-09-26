# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 21:17:06 2018

@author: Administrator
"""

import cv2
import numpy as np 

i=0

while 1 :
    print('The dealing fps is %d.' %(i))
    if i < 10 :
        img=cv2.imread('0000'+str(i)+'.jpg')
    if i >=10 and i < 100 :
        img=cv2.imread('000'+str(i)+'.jpg')
    if i >=100 and i < 1000 :
        img=cv2.imread('00'+str(i)+'.jpg')
    if i >=1000 and i < 10000:
        img=cv2.imread('0'+str(i)+'.jpg')
    if i >=10000 and i < 100000 :
        img=cv2.imread(str(i)+'.jpg')
    img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    a=img.shape[0]
    b=img.shape[1]
    row_center=int(a/2)
    col_center=int(b/2)
    #img=img[row_center-52:row_center+52,col_center-121:col_center+121]
    img=img[row_center-40:row_center+40,col_center-120:col_center+120]
    equ=cv2.equalizeHist(img)
    #cv2.namedWindow('image')
    #cv2.imshow('image2',equ)
    cv2.imshow('image',img)
    if i < 10 :
        img=cv2.imwrite('0000'+str(i)+'.jpg',img)
    if i >=10 and i < 100 :
        img=cv2.imwrite('000'+str(i)+'.jpg',img)
    if i >=100 and i < 1000 :
        img=cv2.imwrite('00'+str(i)+'.jpg',img)
    if i >=1000 and i < 10000:
        img=cv2.imwrite('0'+str(i)+'.jpg',img)
    if i >=10000 and i < 100000 :
        img=cv2.imwrite(str(i)+'.jpg',img)
    print('Resize this photo successfully!')
    i=i+1
    if cv2.waitKey(1) == ord ('q'):
        break
    if i >13116 :
        break
cv2.destroyAllWindows()