# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 20:16:42 2018

@author: Administrator
"""

import cv2
i=0
maxfps=7476 #最后一幅帧图的序号
while 1 :
    print('The dealing fps is %d' %(i))
    if i < 10 :       
        img=cv2.imread('10000'+str(i)+'.jpg')
    if i >= 10 and i < 100 :       
        img=cv2.imread('1000'+str(i)+'.jpg')
    if i >=100 and i < 1000 :       
        img=cv2.imread('100'+str(i)+'.jpg')
    if i >=1000 and i < 10000 :
        img=cv2.imread('10'+str(i)+'.jpg')
    if i >=10000 and i < 100000 :
        img=cv2.imread('1'+str(i)+'.jpg')
    cv2.namedWindow('image')
    cv2.imshow('image',img)
    if i < 10 :
        cv2.imwrite('000'+str(i)+'.jpg',img)
    if i >= 10 and i < 100 :
        cv2.imwrite('00'+str(i)+'.jpg',img)
    if i >=100 and i < 1000 :
        cv2.imwrite('0'+str(i)+'.jpg',img)
    if i >=1000 and i < 10000 :
        cv2.imwrite(str(i)+'.jpg',img)  
    if i >=10000 and i < 100000 :
        cv2.imwrite(str(i)+'.jpg',img)
    i=i+1
    if cv2.waitKey(1) == ord('q'):
        break
    if i > maxfps:
        break
cv2.destroyAllWindows()