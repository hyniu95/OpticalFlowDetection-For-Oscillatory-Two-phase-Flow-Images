# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 10:43:13 2018

@author: Administrator

复现LK光流追踪算法（基于金字塔追踪），提取的特征点是SHI-TOMASI角点，基于图片序列进行实验，实现。完成全视频序列的光流追踪，并设置当特征点小于一定数量时重新搜点。实现.
光流点在每次重新搜点时的初始帧进行标号，共100个点（也可设置更多的点），随后按照每个光流点的坐标进行距离建模和二维坐标向量输出，实现。
分成10个部分连续生成光流点位置以及运动距离数值序列文件，实现。
按照设定的段数在每段的图片序列内进行光流点计算，当每段内的光流点数小于一定数量时重新搜点，并生成坐标序列值自动生成10个数值文件，实现。
对200_01进行光流点数据提取。
"""
import cv2
import numpy as np
global fps,fpm,part,part1

fps=1          #设置起始帧 和oldframe对应 
fpm=0          #不用管
part=1         #命名变量 不用管
part1=int(16939/10)   #图片序列分10段 每段1693帧
minval=50  #每帧中最少应该搜到的光流点数 小于此值重新搜点
maxfps=16939  #读取的帧数 （前提是图片从0开始命名）

feature_params=dict(maxCorners=100, #100
                    qualityLevel=0.01,  #0.3
                    minDistance=3,
                    blockSize=2)
lk_params=dict(winSize=(3,3),
               maxLevel=2,
               criteria=(cv2.TERM_CRITERIA_EPS|cv2.TERM_CRITERIA_COUNT,10,0.03))
def main():
    global fps,fpm,part
    old_frame=cv2.imread('00000.jpg')  
    old_gray=cv2.cvtColor(old_frame,cv2.COLOR_BGR2GRAY)
    #old_gray=cv2.equalizeHist(old_gray)
    p0=cv2.goodFeaturesToTrack(old_gray,mask=None,**feature_params)
    mask=np.zeros_like(old_frame)
    #file=open('200_glycerinum_data'+str(part)+'.txt','a')
    #file.close()
    while(1):
        mean = 0 
        print('The present dealing fps is %d.' %(fps))
        if fps < 10 :
            frame = cv2.imread('0000'+str(fps)+'.jpg')
        if fps >= 10 and fps < 100 :
            frame = cv2.imread('000'+str(fps)+'.jpg')
        if fps >= 100 and fps < 1000 :
            frame = cv2.imread('00'+str(fps)+'.jpg')
        if fps >= 1000 and fps < 10000 :
            frame = cv2.imread('0'+str(fps)+'.jpg')
        if fps >= 10000 and fps < 100000 :
            frame = cv2.imread(str(fps)+'.jpg')
        #equ=cv2.equalizeHist(frame)
        frame_gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        for oo in range(frame_gray.shape[0]):
            for pp in range(frame_gray.shape[1]):
                mean= mean + frame_gray[oo,pp]
        mean=mean/(frame_gray.shape[0]*frame_gray.shape[1])
        ret,binary=cv2.threshold(frame_gray,0,255,cv2.THRESH_BINARY|cv2.THRESH_TRIANGLE)
        for mm in range(binary.shape[0]):
            for nn in range(binary.shape[1]):
                if binary[mm,nn] == 255 :
                    frame_gray[mm,nn] = int(mean)
        
        #frame_gray=cv2.equalizeHist(frame_gray)
        p1,st,err=cv2.calcOpticalFlowPyrLK(old_gray,frame_gray,p0,None,**lk_params)
        good_new=p1[st==1]
        good_old=p0[st==1]
        print(good_new.shape[0])
        if good_new.shape[0] <= minval and fps % part1 !=0 :     #在当前段中如果光流点小于一定数量，则重新进行搜点。
            fpm=fps
            if fpm < 10 :
                old_frame = cv2.imread('0000'+str(fpm)+'.jpg')
            if fpm >= 10 and fpm < 100 :
                old_frame = cv2.imread('000'+str(fpm)+'.jpg')
            if fpm >= 100 and fpm < 1000 :
                old_frame = cv2.imread('00'+str(fpm)+'.jpg')
            if fpm >= 1000 and fpm < 10000 :
                old_frame = cv2.imread('0'+str(fpm)+'.jpg')
            if fpm >= 10000 and fpm < 100000 :
                old_frame = cv2.imread(str(fpm)+'.jpg')
            old_gray=cv2.cvtColor(old_frame,cv2.COLOR_BGR2GRAY)
            p0=cv2.goodFeaturesToTrack(old_gray,mask=None,**feature_params)
            print('Updating new data...')
            #file=open('200_glycerinum_data1.txt','a')
            #file.write('\n update new fps \n')
            #file.close
            fps=fps+1
            continue
        if fps == 1 or fpm == fps-1 :
            good_new_1=p0.reshape(-1,2)*st         #所有追踪点的对应起初位置，按照序号排列，允许存在零点，即非特征点。
            good_old_1=p0.reshape(-1,2)*st
        good_storage=good_new_1.copy()
        if fps % part1 == 0 :                #每计算完每段的帧数后，重新开始下一段搜点。   
            fpm=fps
            part=part+1
            if fpm < 10 :
                old_frame = cv2.imread('0000'+str(fpm)+'.jpg')
            if fpm >= 10 and fpm < 100 :
                old_frame = cv2.imread('000'+str(fpm)+'.jpg')
            if fpm >= 100 and fpm < 1000 :
                old_frame = cv2.imread('00'+str(fpm)+'.jpg')
            if fpm >= 1000 and fpm < 10000 :
                old_frame = cv2.imread('0'+str(fpm)+'.jpg')
            if fpm >= 10000 and fpm < 100000 :
                old_frame = cv2.imread(str(fpm)+'.jpg')
            old_gray=cv2.cvtColor(old_frame,cv2.COLOR_BGR2GRAY)
            p0=cv2.goodFeaturesToTrack(old_gray,mask=None,**feature_params)
            #file=open('200_glycerinum_data'+str(part)+'.txt','a')
            #file.close()
            #print('set up a new file %d.' %(part))
            fps=fps+1
        else :
            for m in range(good_old.shape[0]):       #对所有坐标进行遍历更新,非新特征点坐标不变,坐标发生变化的点进行更新存入good_new_1中.
                for n in range(good_old.shape[1]):
                    for o in range(good_new_1.shape[0]):
                        for p in range(good_new_1.shape[1]):
                            if good_old[m][n] == good_new_1[o][p]:
                                good_new_1[o][p]=good_new[m][n]             #中心思想：利用good_new对应的good_old的值在good_new_1中进行查找位置，进而替换成更新的good_new
            good_old_1=good_storage.copy()
            #print('update good_new_1 over!')
            #print(good_new_1-good_old_1)
            for ii,(new_1,old_1) in enumerate(zip(good_new_1,good_old_1)):        #对所有对应点坐标的对应坐标向量和移动距离求解,并进行数据输出、存储。
                e,f=new_1.ravel()
                g,h=old_1.ravel()
                x1=abs(new_1[0]-old_1[0])
                y1=abs(new_1[1]-old_1[1])
                dis2=np.square(x1)+np.square(y1)
                dis2=np.sqrt(dis2)
                x11=new_1[0]-old_1[0]
                y11=new_1[1]-old_1[1]
                #np.set_printoptions(precision=5,linewidth=200000)  #输出默认80个字符，可以调大一点，因此设成了200000.
                #file=open('200_glycerinum_data'+str(part)+'.txt','a')
                #file.write(str(x11)+':')
                #file.write(str(y11)+'  ')
                #file.close()
            #file=open('200_glycerinum_data'+str(part)+'.txt','a')
            #file.write('\n')
            #file.write('\n')
            #file.close()
            for i,(new,old) in enumerate(zip(good_new,good_old)):      #对追踪到的光流点进行遍历，得到前后对应的光流向量的坐标.
               a,b=new.ravel()                                        #对新点的坐标降维度.二维变一维.
               c,d=old.ravel()                                        #对前一帧的坐标降维度,二维变一维.
               x=abs(new[0]-old[0])
               y=abs(new[1]-old[1])
               dis=np.square(x)+np.square(y)
               dis=np.sqrt(dis)
               mask=cv2.line(mask,(a,b),(c,d),(255,255,255),1)    #前后帧对应点画线
               frame=cv2.circle(frame,(a,b),1,(255,255,255),-1)   #新一帧对应点画圈
               img=cv2.add(mask,frame)                            #帧图叠加,叠加后的图有对应点连线,但是很乱,因此不用.
               cv2.namedWindow('deal_video_01')
               cv2.imshow('deal_video_01',frame_gray)
            fps=fps+1
            if fps >= maxfps : 
                print('normal break')     #注意break的缩进,应该是跳出while1.
                break
            print('Saving data successfully!!!\n')
            old_gray=frame_gray.copy()
            p0=good_new.reshape(-1,1,2)             #很重要，置回（-1，1，2）不能忘
        if cv2.waitKey(1) == ord('q'):
            break
    cv2.destroyAllWindows()

if __name__ is "__main__":
    main()