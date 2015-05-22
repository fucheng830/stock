#!/usr/bin/env python
# -*- coding: utf-8 -*-

'股票交易程序'

'''
@var stock_number:股票代码
@var stock_now_price: 股票现价
@var user_money: 用户资金
@var buy_number: 买人数量
@var buy_price: 买人价格

'''
user_money=1000000
stock_number='sz000616'
stock_now_price=11.28
buy_price=11.28
buy_number=1000
sell_price=11.28
sell_number=100
user_stock=0


#买入股票函数
def buy_stock(buy_price,stock_now_price,num):
    
    if buy_price>=stock_now_price:
        buy_money=buy_price*buy_number
        buy_cost=stock_cost(buy_money,0.001)+buy_number*0.001 #计算买入成本函数
        buy_total_money=buy_money+buy_cost
        return [buy_total_money,1]
        '''
        user_now_money=user_money-buy_money-buy_cost
        user_stock=buy_number
        return [user_now_money,buy_money,user_stock]
        '''
    else:
        return [0,0]

def sell_stock(sell_price,stock_now_price,num):
    if sell_price<=stock_now_price:
        sell_money=sell_price*sell_number
        sell_cost=2*stock_cost(sell_money,0.001)+sell_number*0.001
        sell_total_money=sell_money-sell_cost
        return [sell_total_money,1]
    else:
        return [0,0]
    
        '''
        user_now_money=user_money+sell_money-sell_cost
        user_stock=user_stock-sell_number
        return [user_now_money,user_stock]
        '''
   
   
def stock_cost(pay,count):
    if pay*count<=5:
        return 5
    else:
        return pay*count
    

print buy_stock()
  
    


    

