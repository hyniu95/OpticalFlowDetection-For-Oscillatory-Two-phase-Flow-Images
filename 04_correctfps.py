# -*- coding: utf-8 -*-
"""
Created on Fri Dec  7 10:50:34 2018

@author: Administrator

将视频中的每一帧图像按照鼠标的两次点击构成的区域取点保存
"""

import cv2
import numpy as np
global i,point1,point2,point3,frame,m
i=0
m=5275      #每次程序开始时命名的第一帧图片
n=m+1
point1=[0,0]
point2=[0]
point3=[0]

def use_mouse(event,x,y,flags,param):
    global i,frame,m
    global point1,point2,point3
    img=frame.copy()
    if event== cv2.EVENT_LBUTTONDOWN:
        point1[i]=(x,y)
        point2=point1[0]   #左上角坐标
        point3=point1[1]   #右下角坐标
        i=i+1
    if i>1:
        i=0
        print(point2,point3)
        img_width=abs(point2[0]-point3[0])
        img_height=abs(point2[1]-point3[1])
        cut_img=img[point2[1]:point2[1]+img_height,point2[0]:point2[0]+img_width]
        cv2.imwrite('10'+str(m)+'.jpg',cut_img)
        m=m+1

def main():
    global frame,m,n
    while 1:
        frame=cv2.imread(str(n)+'.jpg')
        print('the present fps is %d' %n)
        cv2.namedWindow('image')
        cv2.setMouseCallback('image',use_mouse)
        cv2.imshow('image',frame)
        n=n+1
        if cv2.waitKey()==ord('1'):
            break
    cv2.destroyAllWindows()
    
if __name__ is '__main__':
    main()
