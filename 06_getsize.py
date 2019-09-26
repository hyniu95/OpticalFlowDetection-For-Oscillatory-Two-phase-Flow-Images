# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 16:11:44 2018

@author: Administrator

输出全部图片序列中的最小行列值
"""

import cv2
import numpy as np
i=0
fps=int(7477) #输入图片数即可 前提是图片命名从0开始


a=np.zeros(fps)
b=np.zeros(fps)

while(1):
    if i > fps-1 :
        print(a.min(),a.max(),b.min(),b.max(),a.argmin(axis=0),b.argmin(axis=0))
        break
    else :
        print('The dealing fps is %d' %(i))
        if i < 10 :
            img = cv2.imread('000'+str(i)+'.jpg')
        if i >= 10 and i < 100 :
            img = cv2.imread('00'+str(i)+'.jpg')
        if i >= 100 and i < 1000 :
            img = cv2.imread('0'+str(i)+'.jpg')
        if i >= 1000 and i < 10000:
            img = cv2.imread(str(i)+'.jpg')
        if i >= 10000:
            img = cv2.imread(str(i)+'.jpg')
        m=img.shape[0]
        n=img.shape[1]
        a[i]=m
        b[i]=n
        i=i+1