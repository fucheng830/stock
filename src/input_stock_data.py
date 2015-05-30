#!/usr/bin/env python
# -*- coding: utf-8 -*-

import types  
import numpy as np
import matplotlib.pyplot as plt
import pylab as pl
from stock_transaction.deal import Deal
import math
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

#移动平均线计算函数
def ma(y,n=5):
    ma=[]
    for line in str_to_float(y,n):
        if len(line) != 0:
            l_average=sum(line)/len(line)
            ma.append(l_average)
        else:
            ma.append(0)
    return ma

#字符串转换浮点数函数   
def str_to_float(y,n):
    b=[]
    for i,x in enumerate(y):
        a=[]
        for l in y[i-n:i]:
            a.append(float(l))
        b.append(a)
    return b
    

#移动平均线指标画图函数
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
 
    





def max_buy(money,price):
    fixPrice=price*(1+0.0003)
    #return money/fixPrice
    return math.floor(money/fixPrice)
        

def make_deal(orginal_money,market):
    myDeal = Deal(money=orginal_money,stock_num=0,rate=0.0003)
    x,y=input_data()
    #ma5=ma(y)
    #ma10=ma(y,n=10)
    ma5=limit(ma(y),4700,5000)
    ma10=limit(ma(y,n=10),4700,5000)
    y=limit(y,4700,5000)
    
    b=[]
    assets=[]
    deal_buy_x=[]
    deal_buy_y=[]
    deal_sell_x=[]
    deal_sell_y=[]
    
    for index,nowprice in enumerate(y):
        
        b.append(nowprice)
        ma5[index]
        ma10[index]
        
        if  index >10 and ma5[index-1]>=ma5[index] and ma5[index]>=ma10[index] and myDeal.money>float(nowprice):
            num=max_buy(myDeal.money,float(nowprice))
            #rest=myDeal.do_deal('buy',float(nowprice),float(nowprice),num,market)
            print "买入价格%s"%float(nowprice)
            print "买入数量%s"%num
            deal_return=myDeal.do_deal('buy',float(nowprice),float(nowprice),num,market)
            deal_buy_x.append(index)
            deal_buy_y.append(float(nowprice))
            
           
            
        elif index>10 and ma5[index-1]<=ma5[index] and ma5[index]<=ma10[index] and myDeal.stock_num>1 :
            num=myDeal.stock_num
            print "卖出%s"%num
            deal_return=myDeal.do_deal('sell',float(nowprice),float(nowprice),num,market) 
            deal_sell_x.append(index)
            deal_sell_y.append(float(nowprice))
            
        else:
           pass 
        
        assets.append([myDeal.stock_num*float(nowprice)+myDeal.money])
            
    return y,ma5,ma10,assets,deal_buy_x,deal_buy_y,deal_sell_x,deal_sell_y 

def make_deal2(orginal_money,market):
    myDeal = Deal(money=orginal_money,stock_num=0,rate=0.0003)
    x,y=input_data()
    #ma5=ma(y)
    #ma10=ma(y,n=10)
    ma5=limit(ma(y),4700,5000)
    ma10=limit(ma(y,n=10),4700,5000)
    y=limit(y,4700,5000)
    
    b=[]
    assets=[]
    deal_buy_x=[]
    deal_buy_y=[]
    deal_sell_x=[]
    deal_sell_y=[]
    
    for index,nowprice in enumerate(y):
        
        b.append(nowprice)
        ma5[index]
        ma10[index]
        
        if  index >10 and float(nowprice)>ma5[index] and myDeal.money>float(nowprice):
            num=max_buy(myDeal.money,float(nowprice))
            #rest=myDeal.do_deal('buy',float(nowprice),float(nowprice),num,market)
            print "买入价格%s"%float(nowprice)
            print "买入数量%s"%num
            deal_return=myDeal.do_deal('buy',float(nowprice),float(nowprice),num,market)
            deal_buy_x.append(index)
            deal_buy_y.append(float(nowprice))
            
           
            
        elif index>10 and float(nowprice)<ma5[index] and myDeal.stock_num>1 :
            num=myDeal.stock_num
            print "卖出%s"%num
            deal_return=myDeal.do_deal('sell',float(nowprice),float(nowprice),num,market) 
            deal_sell_x.append(index)
            deal_sell_y.append(float(nowprice))
            
        else:
           pass 
        
        assets.append([myDeal.stock_num*float(nowprice)+myDeal.money])
            
    return y,ma5,ma10,assets,deal_buy_x,deal_buy_y,deal_sell_x,deal_sell_y 
    
def make_chart_assets(x,var1,var2,var3,var4,buyX,buyY,sellX,sellY):
   pl.figure(dpi=80) 
   a1=pl.subplot(211)
   pl.plot(x,var1,'-',color='red')
   pl.plot(x,var2,'-', color='cyan')
   pl.plot(x,var3,'-',color='yellow')
   #pl.plot(buyX,buyY,'.',color='magenta')
   #pl.plot(sellX,sellY,'.',color='black')
   pl.scatter(buyX,buyY, color ='blue')
   pl.scatter(sellX,sellY,color ='black')
   #pl.scatter(buyX,buyY)
   #pl.scatter(sellX,sellY)
   
   a2=pl.subplot(212)
   pl.plot(x,var4,'-',color='blue')
   
 
   pl.show()        


#var1,var2,var3,var4=make_deal(orginal_money=100000, market='sz') 

#make_chart_assets(range(len(var1)),var1,var2,var3,var4)
'''
x,y=input_data()
ma5=limit(ma(y,5),4900,5000)
ma10=limit(ma(y,10),4900,5000)
y=limit(y,4900,5000)
make_chart(range(len(ma5)),ma5,ma10,y)
'''
    
var1,var2,var3,var4,buyX,buyY,sellX,sellY=make_deal(orginal_money=100000, market='sz')

#np.shape()
make_chart_assets(range(len(var1)),var1,var2,var3,var4,buyX,buyY,sellX,sellY)

#print max_buy(100000,17.54) 
#myDeal=Deal(money=100000,stock_num=0,rate=0.0003)
#print myDeal.do_deal('buy',17.54,17.54,5684,market="sz")   
#print myDeal.cost(17.54, 5684, market="sz", behavior='buy', rate=0.0003) 
        
    