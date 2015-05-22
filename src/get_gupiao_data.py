#!/usr/bin/env python
# -*- coding: utf-8 -*-

'股票交易程序 获取股票接口数据'

'''
  `id` int(100) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `name` varchar(100) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL COMMENT '股票名称',
  `stock_number` int(10) NOT NULL COMMENT '股票代码',
  `now_price` float(20) NOT NULL COMMENT '当前价格',
  `yesterday_price`  float(20) NOT NULL COMMENT '昨收',
  `today_start_price`  float(20) NOT NULL COMMENT '今开',
  `today_deal_num`
  `positive_buy` int(20) NOT NULL COMMENT '外盘',
  `positive_sell` int(20) NOT NULL COMMENT '内盘',
  `buy_one` float(20) NOT NULL COMMENT '买一',
  `buy_one_number` int(20) NOT NULL COMMENT '买一量（手）',
   `buy_two` float(20) NOT NULL COMMENT '买二',
  `buy_two_number` int(20) NOT NULL COMMENT '买二量（手）',
   `buy_three` float(20) NOT NULL COMMENT '买三',
  `buy_three_number` int(20) NOT NULL COMMENT '买三量（手）',
   `buy_four` float(20) NOT NULL COMMENT '买四',
  `buy_four_number` int(20) NOT NULL COMMENT '买四量（手）',
   `buy_five` float(20) NOT NULL COMMENT '买五',
  `buy_five_number` int(20) NOT NULL COMMENT '买五量（手）',
  `sell_one` float(20) NOT NULL COMMENT '卖一',
  `sell_one_number` int(20) NOT NULL COMMENT '卖一量（手）',
  `sell_two` float(20) NOT NULL COMMENT '卖二',
  `sell_two_number` int(20) NOT NULL COMMENT '卖二量（手）',
  `sell_three` float(20) NOT NULL COMMENT '卖三',
  `sell_three_number` int(20) NOT NULL COMMENT '卖三量（手）',
  `sell_four` float(20) NOT NULL COMMENT '卖四',
  `sell_four_number` int(20) NOT NULL COMMENT '卖四量（手）',
  `sell_five` float(20) NOT NULL COMMENT '卖五',
  `sell_five_number` int(20) NOT NULL COMMENT '卖五量（手）',
  `recent_deal` int(20) NOT NULL COMMENT '最近逐笔成交',
  `z_time` varchar(30) NOT NULL COMMENT '时间',
  `up_down` float(20) NOT NULL COMMENT '涨跌',
  `up_down_percent` float(20) NOT NULL COMMENT '涨跌%',
  `highest_price` float(20) NOT NULL COMMENT '最高',
  `lowest_price` float(20) NOT NULL COMMENT '最低 ',
  `price_number_average` float(20) NOT NULL COMMENT '价格/成交量（手）/成交额 ',
  `deal_number` int(20) NOT NULL COMMENT '成交量（手）',
  `deal_money` int(20) NOT NULL COMMENT '成交额（万）',
  `chang_percent` float(20) NOT NULL COMMENT '换手率',
  `market_gain_percent` float(20) NOT NULL COMMENT '市盈率',
  `not_know` int(20) NOT NULL COMMENT '空',
  `heighest_price` float(20) NOT NULL COMMENT '最高',
  `lower_price` float(20) NOT NULL COMMENT '最低',
  `shake` float(20) NOT NULL COMMENT '振幅',
  `circulate_money` int(20) NOT NULL COMMENT '流通市值',
  `total_money` int(20) NOT NULL COMMENT '总市值',
  `maket_absolute_percent` float(20) NOT NULL COMMENT '市净率',
  `up_stop_price` float(20) NOT NULL COMMENT '涨停价',
  `down_stop_price` float(20) NOT NULL COMMENT '跌停价',
  `get_time` varchar(20) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL COMMENT '更新时间',

'''

import urllib2
import sys
import re
import mysql.connector


#table=(id,name,stock_number,now_price,yesterday_price,today_start_price,positive_buy,positive_sell,buy_one,buy_one_number,buy_two,buy_two_number,buy_three,buy_three_number,buy_four,buy_four_number,buy_five,buy_five_number,sell_one,sell_one_number,sell_two,sell_two_number,sell_three,sell_three_number,sell_four,sell_four_number,sell_five,sell_five_number,recent_deal,z_time,up_down,up_down_percent,highest_price,lowest_price,price_number_average,deal_number,deal_money,chang_percent,market_gain_percent,not_know,heighest_price,lower_price,shake,circulate_money,total_money,maket_absolute_percent,up_stop_price,down_stop_price,get_time)
req = urllib2.Request('http://qt.gtimg.cn/q=sz000858')
response = urllib2.urlopen(req)
the_page = response.read().decode('GBK')
a=re.split(r'[~]',the_page)
print a

conn = mysql.connector.connect(user='root',password='',database='gupiao',use_unicode=True)
cursor = conn.cursor()

cursor.execute('insert into shuju (id,name,stock_number,now_price,yesterday_price,today_start_price,today_deal_num,positive_buy,positive_sell,buy_one,buy_one_number,buy_two,buy_two_number,buy_three,buy_three_number,buy_four,buy_four_number,buy_five,buy_five_number,sell_one,sell_one_number,sell_two,sell_two_number,sell_three,sell_three_number,sell_four,sell_four_number,sell_five,sell_five_number,recent_deal,z_time,up_down,up_down_percent,highest_price,lowest_price,price_number_average,deal_number,deal_money,chang_percent,market_gain_percent,not_know,heighest_price,lower_price,shake,circulate_money,total_money,maket_absolute_percent,up_stop_price,down_stop_price,get_time) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',a)
cursor.rowcount

conn.commit()
cursor.close()

cursor = conn.cursor()
cursor.execute('select * from shuju where id = 1')
values=cursor.fetchall()
print values
cursor.close()
conn.close()




