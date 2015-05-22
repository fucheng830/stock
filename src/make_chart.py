#!/usr/bin/env python
# -*- coding: utf-8 -*-

'股票交易程序   画图模块'

from matplotlib.pyplot import *
import matplotlib.pyplot as plt
import pylab as pl
import mysql.connector
'''
plot([0, 1], [0, 1])      # plot a line from (0, 0) to (1, 1)
title("a strait line")
xlabel("x value")
ylabel("y value")
savefig("demo.png")
'''

def sql_get_stock_data():
    conn = mysql.connector.connect(user='root',password='',database='gupiao',use_unicode=True)
    cursor = conn.cursor()
    #cursor.execute('SELECT * FROM shuju1 where stock_number = 601318 limit 10')
    sql='select now_price,z_time  from shuju1 where stock_number = 601318 limit 1000'
    cursor.execute(sql)
    rows = cursor.fetchall()
    stock_data=[]
    i=0
    for row in rows :
        i+=6 
        #time=row[1].encode('utf-8')
        #s1 = int(time)
        stock_data.append([i,row[0]])
        #print row
    conn.commit() 
    cursor.close()
    
    return stock_data

stock_data=sql_get_stock_data()
x=[]
y=[]
for a,b in stock_data:
    x.append(a)
    y.append(b)

pl.plot(x,y)
pl.show()

'''
x = [1, 2, 3, 4, 5]# Make an array of x values
y = [1, 4, 9, 16, 25]# Make an array of y values for each x value
pl.plot(x, y)# use pylab to plot x and y
pl.show()# show the plot on the screen
'''