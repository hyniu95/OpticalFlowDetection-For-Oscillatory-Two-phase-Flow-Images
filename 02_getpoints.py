# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 15:10:04 2018

@author: Administrator

实现了加载图片以及利用鼠标进行图像区域交互并进行剪裁并另存为新图片的操作
"""

import cv2
import numpy as np  
global img
global point1
global point2,i
i=0
def use_mouse(event,x,y,flags,param):              #参数必须要写好 不写编译不通过
    global img
    global point1
    global point2
    if event==cv2.EVENT_LBUTTONDOWN:
        point1=(x,y)
        print(point1)
        cv2.circle(img,point1,1,(255,255,255),1)
    elif event==(cv2.EVENT_FLAG_LBUTTON):
        point2=(x,y)
        cv2.rectangle(img,point1,point2,(255,255,255),1)
    elif event==cv2.EVENT_LBUTTONUP:
        point2=(x,y)
        print(point2)
        cv2.rectangle(img,point1,point2,(255,255,255),1)
        #img_width=abs(point1[0]-point2[0])
        #img_height=abs(point1[1]-point2[1])
       #print('value is %d' %(point1[1]+img_height))
        #img1=img[point1[1]+1:point1[1]+img_height,point1[0]+1:point1[0]+img_width]   #python中建坐标是横x竖y 但是在切片中先写y再写x
        #cv2.imwrite('10'+str(i)+'.jpg',img1)

def main():
    global img,i
    img=cv2.imread(str(i)+'.jpg')
    img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    cv2.namedWindow('image')
    cv2.setMouseCallback('image',use_mouse)
    while True:
        cv2.imshow('image',img)
        if cv2.waitKey(1)==ord('1'):
            break
    cv2.destroyAllWindows()
    
if __name__=="__main__":
    main()