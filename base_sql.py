#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 11:13:35 2018

@author: pyh
"""

class mysql_data:
    def __init__(self,user_name,password):
        self.conn=pymysql.connect(host='127.0.0.1',
                 port=3306,
                 user=user_name,
                 passwd=password,
                 charset='utf8')
        self.cursor=self.conn.cursor()
        
    def create_DATABASE(self,db_name):
        self.cursor.execute('drop database if exists '+db_name)
        self.cursor.execute('create database '+db_name)
        self.cursor.execute('use '+db_name)
        
    def delete_DATABASE(self,db_name):
        self.cursor.execute('drop database if exists '+db_name)

    def use_DATABASE(self,db_name):
        try:
             self.cursor.execute('use '+db_name)
        except:
             print('use new database failed')
    
    def show_DATABASE(self):
        self.cursor.execute('show databases')
        return self.cursor.fetchall()
        
    def create_TABLE(self,name,content):
        self.cursor.execute('drop table if exists '+name)
        self.cursor.execute('create table '+name+'('+content+')')
        
    def insert_TABLE(self,table,value):
        self.cursor.execute('insert into '+table+' values('+value+')')
        self.conn.commit()
        
    def delete_TABLE(self,table_name):
        self.cursor.execute('drop table if exists '+table_name)
        
    def show_TABLE(self,table_name):
        self.cursor.execute('select * from '+table_name)
        return self.cursor.fetchall()
        
    def close(self):
        self.cursor.close()
        self.conn.close()
    

#import pymysql
#db=mysql_data('root','622825')
#db.create_DATABASE('test5')
#db.use_DATABASE('test1')
#db.create_TABLE('hh','id int,name varchar(20) charset utf8')
#db.insert_TABLE('hh(id,name)',"11,'苏打'")
#db.insert_TABLE('hh(id,name)',"12,'sss'")
#print(db.show_DATABASE())
#print(db.show_TABLE('hh'))
#db.delete_TABLE('hh')
#db.close()

import pymysql
from init import *

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
db.create_DATABASE('base')    
db.create_TABLE('station',define_table[0:-2])

for i in range(len(value)):
    print(i)
    db.insert_TABLE('station('+using_table[0:-2]+')',value[i])
    
print(db.show_TABLE('station'))

    
