#!/usr/bin/env python
# -*- coding: utf-8 -*-

'股票交易程序   开始程序'

import time
import re


def the_time():
    alltime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    now_point_time = time.mktime(time.strptime(alltime,"%Y-%m-%d %H:%M:%S")) 
    now_time=re.split(r' ',alltime)
    today=now_time[0]
    s_time=today+' '+'09:30:00'
    e_time=today+' '+'23:45:00'
    start_point_time=time.mktime(time.strptime(s_time,"%Y-%m-%d %H:%M:%S"))
    end_point_time=time.mktime(time.strptime(e_time,"%Y-%m-%d %H:%M:%S"))
    return [start_point_time,now_point_time,end_point_time]

def start_time():
    m_time = the_time()
    if m_time[0]==m_time[1]:
        print '开始运行程序'
        
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
            
            time.sleep(6)
            start_time(m_time)
        
        
        
'''       
alltime=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
b = time.mktime(time.strptime(alltime,"%Y-%m-%d %H:%M:%S"))
a=the_time()

print a[0],a[1]
'''

start_time()










