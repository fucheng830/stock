#!/usr/bin/env python
# -*- coding: utf-8 -*-

'股票交易程序   获取股票脚本'

import urllib2
import sys
import re
import mysql.connector
import time


'''
se=()
the_stock=()
f=open('daima.txt','r')
daima=f.readlines()

'''

#请求股票数据函数返回值为list
def get_stock(market,stock_number):
    url='http://qt.gtimg.cn/q=%s%s'%(market,stock_number)
    req = urllib2.Request(url)
    response = urllib2.urlopen(req)
    the_page = response.read().decode('GBK')
    a=re.split(r'[~]',the_page)
    return a

#插入数据函数
'''
def sql_insert(cursor):
    cursor.execute('insert into shuju (id,name,stock_number,now_price,yesterday_price,today_start_price,today_deal_num,positive_buy,positive_sell,buy_one,buy_one_number,buy_two,buy_two_number,buy_three,buy_three_number,buy_four,buy_four_number,buy_five,buy_five_number,sell_one,sell_one_number,sell_two,sell_two_number,sell_three,sell_three_number,sell_four,sell_four_number,sell_five,sell_five_number,recent_deal,z_time,up_down,up_down_percent,highest_price,lowest_price,price_number_average,deal_number,deal_money,chang_percent,market_gain_percent,not_know,heighest_price,lower_price,shake,circulate_money,total_money,maket_absolute_percent,up_stop_price,down_stop_price,get_time) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',a)
'''
#创建数据连接函数
def sql_conn(a):
    conn = mysql.connector.connect(user='root',password='',database='gupiao',use_unicode=True)
    cursor = conn.cursor()
    
    cursor.execute('insert into shuju (id,name,stock_number,now_price,yesterday_price,today_start_price,today_deal_num,positive_buy,positive_sell,buy_one,buy_one_number,buy_two,buy_two_number,buy_three,buy_three_number,buy_four,buy_four_number,buy_five,buy_five_number,sell_one,sell_one_number,sell_two,sell_two_number,sell_three,sell_three_number,sell_four,sell_four_number,sell_five,sell_five_number,recent_deal,z_time,up_down,up_down_percent,highest_price,lowest_price,price_number_average,deal_number,deal_money,chang_percent,market_gain_percent,not_know,heighest_price,lower_price,shake,circulate_money,total_money,maket_absolute_percent,up_stop_price,down_stop_price,get_time) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',a)
    conn.commit()
    cursor.close()
    conn.close()

    
def sql_close():
    pass

def sql_get_stock_list():
    conn = mysql.connector.connect(user='root',password='',database='gupiao',use_unicode=True)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM stock_number ')
    rows = cursor.fetchall()
    stock_list=[]
    for row in rows:
        stock_list.append([row[2],row[3]])
    conn.commit() 
    cursor.close()
    
    return stock_list
   
    
    '''
    for row in rows:  
        print "%s, %s, %s, %s" % (row[0], row[1], row[2], row[3]) 
        a=get_stock(row[2],row[3])
        cursor = conn.cursor()
        cursor.execute('insert into shuju (id,name,stock_number,now_price,yesterday_price,today_start_price,today_deal_num,positive_buy,positive_sell,buy_one,buy_one_number,buy_two,buy_two_number,buy_three,buy_three_number,buy_four,buy_four_number,buy_five,buy_five_number,sell_one,sell_one_number,sell_two,sell_two_number,sell_three,sell_three_number,sell_four,sell_four_number,sell_five,sell_five_number,recent_deal,z_time,up_down,up_down_percent,highest_price,lowest_price,price_number_average,deal_number,deal_money,chang_percent,market_gain_percent,not_know,heighest_price,lower_price,shake,circulate_money,total_money,maket_absolute_percent,up_stop_price,down_stop_price,get_time) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',a)
        print "Number of rows returned: %d" % cursor.rowcount  
        conn.commit()
        cursor.close()
        
    conn.close()
    '''

#创建数据连接函数
def sql_conn_1(a):
    conn = mysql.connector.connect(user='root',password='',database='gupiao',use_unicode=True)
    cursor = conn.cursor()
    
    cursor.execute('insert into shuju (id,name,stock_number,now_price,yesterday_price,today_start_price,today_deal_num,positive_buy,positive_sell,buy_one,buy_one_number,buy_two,buy_two_number,buy_three,buy_three_number,buy_four,buy_four_number,buy_five,buy_five_number,sell_one,sell_one_number,sell_two,sell_two_number,sell_three,sell_three_number,sell_four,sell_four_number,sell_five,sell_five_number,recent_deal,z_time,up_down,up_down_percent,highest_price,lowest_price,price_number_average,deal_number,deal_money,chang_percent,market_gain_percent,not_know,heighest_price,lower_price,shake,circulate_money,total_money,maket_absolute_percent,up_stop_price,down_stop_price,get_time) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',a)
    
    conn.commit()
    cursor.close()
    conn.close()

#a=sql_get_stock_list()
def start_get():
    a=[['600433','sh'],['601318','sh'],['601258','sh']]
    nowtime=time.time()
    for x in a:
        b=get_stock(x[1],x[0])
        print b
        sql_conn(b)
        lasttime=time.time()
        usedtime=lasttime-nowtime
    return usedtime

def the_time():
    alltime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    now_point_time = time.mktime(time.strptime(alltime,"%Y-%m-%d %H:%M:%S")) 
    now_time=re.split(r' ',alltime)
    today=now_time[0]
    s_time=today+' '+'09:29:00'
    e_time=today+' '+'15:35:00'
    start_point_time=time.mktime(time.strptime(s_time,"%Y-%m-%d %H:%M:%S"))
    end_point_time=time.mktime(time.strptime(e_time,"%Y-%m-%d %H:%M:%S"))
    return [start_point_time,now_point_time,end_point_time]

def start_time():
    m_time = the_time()
    if m_time[0]==m_time[1]:
        print '开始运行程序'
        usedtime=start_get()
        waittime=5-usedtime
        time.sleep(waittime)
        start_time()
        
    elif m_time[0]-m_time[1]>0 :
        last_time=m_time[0]-m_time[1]
        #echo='距离开始还剩'+last_time+'秒'
        print last_time
        time.sleep(last_time)
        start_time(m_time)
    elif m_time[0]-m_time[1]<0 :
        now=m_time[1]-m_time[2]
        print now
        if m_time[1]-m_time[2]>0:
           m_time[0]=m_time[0]+3600*24 
           print '已结束'
           exit
        else:
            print '数据读取中'
            usedtime=start_get()
            waittime=5-usedtime
            time.sleep(waittime)
            start_time()

'''
a=get_stock('sh','600017')

b=get_stock(a[0][1],a[0][0])
sql_conn(b)
#print len(a)
#print len(b)
'''
start_time()