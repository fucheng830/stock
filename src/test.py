#!/usr/bin/env python
# -*- coding: utf-8 -*-

from stock_transaction import db
db.create_engine(user='root', password='', database='gupiao', host='127.0.0.1', port=3306)
user_value = db.select('select * from user_value')
#print '用户:%s' % user_value[0]['user_name'].encode('UTF8')