#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 11:13:35 2018

@author: pyh
"""

import xlrd
from init import *
from mysql_data import *


file_name='基准站配置0305.xlsx'
table_head=['lb','lbxh','zddh','zdmc','jsjIP','ckzbh','jsjbh','txbh','txxh',
            'jsjpp','jsjxh','ssq','dw','zdszfwq','zdszgc','sjbfdk','nwbfdk',
            'gcdlx','sjcsgs','yys','cslx','zdjrsj','dz','kjzdmc','zdbh',
            'gcz','wdyzz','yzz','hxzd','jsjwldlyhm','jsjwydlmm','bz']
date_table_head=['zdjrsj']
db_name='base'
table_name='station'

sheet=xlrd.open_workbook(file_name)
table=sheet.sheets()[0]

ncols=table.ncols
nrows=table.nrows


data=[]   
for i in range(1,nrows):
    data.append([])
    for j in range(ncols):
        data[i-1].append(table.row_values(i)[j])
#          if data[i-1][j]=='':
#            data[i-1][j]='null'
        


define_table=''
using_table=''
for i in range(len(table_head)):
    check=False
    for j in range(len(date_table_head)):        
        if table_head[i]==date_table_head[j]:
            define_table=define_table+table_head[i]+' date, '
            using_table=using_table+table_head[i]+', '
            check=True
    if check:
        continue
    if type(data[0][i])==float:
        define_table=define_table+table_head[i]+' float, '
    elif type(data[0][i])==int:
        define_table=define_table+table_head[i]+' int, '
    else:
        define_table=define_table+table_head[i]+' varchar(80) charset utf8, '
    using_table=using_table+table_head[i]+', '
            
value=[]
for i in range(len(data)):
    sing=''
    for j in range(len(data[0])):
        check=False
        for k in range(len(date_table_head)):
            if table_head[j]==date_table_head[k] and data[i][j]=='':
                sing=sing+"'10000101',"
                check=True
        if check:
            continue
        if type(data[0][j])==float or type(data[0][j])==int:
            if data[i][j]=='':
                data[i][j]=-1
            sing=sing+str(data[i][j])+","
        else:
            sing=sing+"'"+str(data[i][j])+"',"
    value.append(sing[0:-1])
        
db=mysql_data('root','622825')
db.create_DATABASE(db_name)    
db.create_TABLE(table_name,define_table[0:-2])

for i in range(len(value)):
    print('number:%d'%i)
    db.insert_TABLE(table_name+'('+using_table[0:-2]+')',value[i])
    
print(db.show_TABLE(table_name))

db.close()

    
