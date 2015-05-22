#!/usr/bin/env python
# -*- coding: utf-8 -*-

'股票交易程序   获取股票列表'

import mysql.connector

conn = mysql.connector.connect(user='root',password='',database='gupiao',use_unicode=True)
cursor = conn.cursor()
cursor.execute('SELECT * FROM stock_number ')
rows = cursor.fetchall() 
for row in rows:  
    print "%d, %s, %s, %s" % (row[0], row[1], row[2], row[3])  
  
print "Number of rows returned: %d" % cursor.rowcount  

conn.commit()
cursor.close()
conn.close()
