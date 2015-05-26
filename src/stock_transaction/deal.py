#!/usr/bin/python
# -*- coding:utf-8 -*-

'''
Created on 2015年5月11日

@author: fucheng
印花税:0.001 sell收取
过户费:1 or 0.001*num sh收取
佣金:5 or 0.003 可为变量

'''

class Deal(object):
    
    '''
            股票模拟交易程序
    '''
    def __init__(self,money,stock_num,rate):
        '''
                        构造函数
        '''
        self.money = money
        self.stock_num = stock_num
        self.rate = rate
        self.tax=0.001
        
        
    def do_deal(self,behavior,price,stock_price,num,market):
        if behavior=='buy':
            if price>=stock_price:
                buy_money=price*num+self.cost(price,num,market,behavior,self.rate)
                self.stock_num=self.stock_num+num
                self.money=self.money-buy_money
                return [buy_money,self.stock_num,self.money]
            else:
                return [0,0]
        elif behavior=='sell':
            if price>=stock_price and self.stock_num >= num:
                sell_money=price*num-self.cost(price,num,market,behavior,self.rate)
                self.stock_num=self.stock_num-num
                self.money=self.money+sell_money
                return [sell_money,self.stock_num,self.money]
            else:
                return [0,0]
    
    def cost(self,price,num,market,behavior,rate):
        if behavior=='buy':
            if market=='sh':
                if num<=1000:
                    if price*num*rate<=5:
                        cost=1+5
                    elif price*num*rate>5:
                        cost=1+price*num*rate
                    else:
                        message="num or rate or price数据类型错误"
                        return  message
                elif num>1000:
                    if price*num*rate<=5:
                        cost=0.001*num+5
                    elif price*num*rate>5:
                        cost=0.001*num+price*num*rate
                    else:
                        message="num or rate or price数据类型错误"
                        return  message
                else:
                    message="num数据类型错误"
                    return  message
                
            elif market=='sz':
                if price*num*rate<=5:
                    cost=5
                elif price*num*rate>5:
                    cost=price*num*rate
                else:
                    message="num or rate or price数据类型错误"
                    return  message
            
        if behavior=='sell':
            if market=='sh':
                if num<=1000:
                    if price*num*rate<=5:
                        cost=1+5+self.tax*num
                    elif price*num*rate>5:
                        cost=1+price*num*rate+self.tax*num
                    else:
                        message="num or rate or price数据类型错误"
                        return  message
                elif num>1000:
                    if price*num*rate<=5:
                        cost=0.001*num+5+self.tax*num
                    elif price*num*rate>5:
                        cost=0.001*num+price*num*rate+self.tax*num
                    else:
                        message="num or rate or price数据类型错误"
                        return  message
                else:
                    message="num数据类型错误"
                    return  message
                
            if market=='sz':
                if price*num*rate<=5:
                    cost=5+self.tax*num
                elif price*num*rate>5:
                    cost=price*num*rate+self.tax*num
                else:
                    message="num or rate or price数据类型错误"
                    return  message
        return cost
    
if __name__ == '__main__':

    num=10000
    price=10
    stock_price=10
    market='sh'
    behavior='sell'
    rate=0.0003
    a=Deal(price,stock_price,num,market,behavior,rate)
    print a.do_deal()
    

   
        

        