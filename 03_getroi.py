# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 19:31:20 2018

@author: Administrator

实现透明腔中的目标追踪  BUG：光流点小于3个时 未完成继续追踪 针对200_01的原始程序
"""

import cv2
import numpy as np
global m

a0=np.array([[4,123],[253,123],[4,33],[253,33]],dtype='float32')   # 200_01 很重要，原来LK算法输入的坐标点都是二维坐标，并且一定要float32位！
#a0=np.array([[5,414],[249,414],[5,522],[249,522]],dtype='float32')
a0=a0.reshape(-1,1,2)
lk_params=dict(winSize=(20,20),
               maxLevel=2,
               criteria=(cv2.TERM_CRITERIA_EPS|cv2.TERM_CRITERIA_COUNT,10,0.03))
feature_params=dict(maxCorners=4, #100
                    qualityLevel=0.1,  #0.3
                    minDistance=7,
                    blockSize=7)
m=2
name=0
def main() :
    global m,a0,name
    x_center=0
    y_center=0
    old_frame=cv2.imread('1.jpg')
    old_frame_gray=cv2.cvtColor(old_frame,cv2.COLOR_BGR2GRAY)
    while 1 :
        print('The dealing fps is %d' %(m))
        dis_x=np.zeros(a0.shape[0],dtype='int')
        dis_y=np.zeros(a0.shape[0],dtype='int')
        mask=np.zeros_like(old_frame)
        frame=cv2.imread(str(m)+'.jpg')
        frame_gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        p1,st,err=cv2.calcOpticalFlowPyrLK(old_frame_gray,frame_gray,a0,None,**lk_params)
        good_new=p1[st==1]
        good_old=a0[st==1]
        if good_new.shape[0] == 3:
            print('The present updating fps is %d' %(m))
            a0=np.array([[x_center-122,y_center-42],[x_center-122,y_center+42],[x_center+122,y_center-42],[x_center+122,y_center+42]],dtype='float32')
            a0=a0.reshape(-1,1,2)
            continue
        #if good_new.shape[0] == 2:
            #print('The present updating fpsfps is %d' %(m))
            #a0==np.array([[x_center-122,y_center-52],[x_center+122,y_center-52]])
            #a0=a0.reshape(-1,1,2)
            #continue
        for i,(x,y) in enumerate(zip(good_new,good_old)):
            a,b=x.ravel()
            c,d=y.ravel()
            dis_x[i]=int(a)
            dis_y[i]=int(b)
            cv2.circle(frame,(a,b),1,(0,0,255),2)
        x_center=0
        y_center=0
        for mm in dis_x:
            x_center=x_center+mm
        for nn in dis_y:
            y_center=y_center+nn
        x_center=x_center/4
        y_center=y_center/4
        x_center=int(x_center)
        y_center=int(y_center)
        q=x_center-122
        w=y_center-52
        e=x_center+122
        r=y_center+52
        if q <=0:
            q=0
        if w <=0:
            w=0
        if e >= frame_gray.shape[1]:
            e=frame_gray.shape[1]
        if r >= frame_gray.shape[0]:
            r=frame_gray.shape[0]
        cv2.rectangle(mask,(q,w),(e,r),(0,255,255),2)
        img2=frame_gray[w:r,q:e]
        '''
        if name < 10:
            cv2.imwrite('10000'+str(name)+'.jpg',img2)
        if name >=10 and name < 100 :
            cv2.imwrite('1000'+str(name)+'.jpg',img2)
        if name >=100 and name < 1000 :
            cv2.imwrite('100'+str(name)+'.jpg',img2)
        if name >=1000 and name < 10000 :
            cv2.imwrite('10'+str(name)+'.jpg',img2)
        if name >=10000 and name < 100000 :
            cv2.imwrite('1'+str(name)+'.jpg',img2)
        print('Saved photos successfully!')
        '''
        img=cv2.add(mask,frame)
        cv2.namedWindow('image')
        cv2.imshow('image',img)
        m=m+1
        name=name+1
        a0=good_new.reshape(-1,1,2)             #important,the ao must be a 2D vector
        old_frame_gray=frame_gray.copy()         #'copy' this word is important
        if cv2.waitKey(1) == ord('q'):
            break
        if m > 18559:
            break
    cv2.destroyAllWindows()

if __name__ is "__main__" :
    main()
    

        
        
