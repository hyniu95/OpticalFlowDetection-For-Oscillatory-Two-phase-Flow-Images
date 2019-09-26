# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 19:46:07 2018

@author: Administrator

实现了加载视频以及将视频中的每一帧图像取出的操作
"""

import cv2

i=0
cap=cv2.VideoCapture('600_02.avi')

while(1):
    ret,frame=cap.read()
    if ret is False :
        break
    frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    i=i+1
    cv2.namedWindow('img')
    cv2.imshow('img',frame)
    cv2.imwrite(str(i)+'.jpg',frame)
    if cv2.waitKey(1)==ord('q'):                  #每过n毫秒刷新一次 实现自动播放 可快进 可慢播
        break
cv2.destroyAllWindows()
cap.release()