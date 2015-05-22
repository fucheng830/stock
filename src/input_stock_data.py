#!/usr/bin/env python
# -*- coding: utf-8 -*-

import types  
import numpy as np
import matplotlib.pyplot as plt
import pylab as pl
'''
fr = open(filename)
    numberOfLines = len(fr.readlines())         #get the number of lines in the file 
    returnMat = zeros((numberOfLines,3))        #prepare matrix to return 返回的列阵 zeros()，初始化为0
    classLabelVector = []                       #prepare labels return   
    fr = open(filename)
    index = 0
    for line in fr.readlines():
        line = line.strip()#删除开头和结尾的空白字符（包括'\n', '\r',  '\t',  ' ')
        listFromLine = line.split('\t')#以空格分割字符串
        returnMat[index,:] = listFromLine[0:3]#将初始化的列阵赋值
        classLabelVector.append(changelabels(listFromLine[-1]))#listFromLine[-1]倒数第一个元素
        index += 1
    return returnMat,classLabelVector
'''

def input_data():
    x=[]
    y=[]
    with open('stock_data/pinganData.XLS','r') as f:
       
        for index,line in enumerate(f.readlines()):
            if index==0 :
                pass
            else: 
                line=line.split('\t')
                x.append(index)
                y.append(line[4])
    return x,y

def limit(v_list,start,end):
    list=[]
    for i,l in enumerate(v_list):
        if i>=start and i<=end:
           list.append(l)
          
        else:
           pass 
    return list

def ma(y,n=5):
    ma=[]
    for line in str_to_float(y,n):
        if len(line) != 0:
            l_average=sum(line)/len(line)
            ma.append(l_average)
        else:
            ma.append(0)
    return ma
   
def str_to_float(y,n):
    b=[]
    for i,x in enumerate(y):
        a=[]
        for l in y[i-n:i]:
            a.append(float(l))
        b.append(a)
    return b
    

    
 
def make_chart(x,var1,var2,var3):
   pl.plot(x,var1, '-', color='yellow')
   pl.plot(x,var2,'-', color='cyan')
   pl.plot(x,var3,'-',color='red')
   pl.title(u'pingan') 
   pl.xlabel(u'time')
   pl.ylabel(u'price')
   pl.show()
   #pl.xlim(0.0, 7.0)# set axis limits
   #pl.ylim(0.0, 30.)
 
    

x,y=input_data()
ma5=limit(ma(y,5),4900,5000)
ma10=limit(ma(y,10),4900,5000)
y=limit(y,4900,5000)
make_chart(range(len(ma5)),ma5,ma10,y)

def test1():
    pass
    