#!/usr/bin/env python
# -*- coding: utf-8 -*-

'股票交易程序   输入股票代码脚本'

import os
import re
import mysql.connector




'''
f=open('price_num.txt','r')
res=f.read().decode('GBK')
a=re.split(r'[)]',res)
print a
'''

def readtxt(text_name):
    f=open(text_name,'r')
    res=f.readlines()
    lines=[]
    for line in res:
        a=re.split(r'\t',line)
        a.insert(0, '')
        the_line=[]
        i=0
        for li in a:
            if i<7:
                i+=1
                the_line.append(li)
            else:
                li=re.subn(r'\n',' ', li)
                the_line.append(li[0])
         
        #print the_line
        #sql=
        mysql_insert(the_line)
    
def mysql_insert(the_line):
    conn = mysql.connector.connect(user='root',password='',database='gupiao',use_unicode=True)
    cursor = conn.cursor()
    cursor.execute('insert into price_num (pn_id,day_time,start_price,top_price,down_price,end_price,deal_num,deal_money) values (%s,%s,%s,%s,%s,%s,%s,%s)',the_line)
    cursor.rowcount
    conn.commit()
    cursor.close()
    conn.close()
    
'''
the_stock=[]
for b in a:
    k=re.split(r'[(]',b)
    the_stock.append(k)

for the_list in the_stock:
    a=['',the_list[0],the_list[1],'sz']
    mysql_insert(a)
'''
readtxt('price_num.txt')   
 
    
    




