#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 12:41:02 2018

@author: pyh
"""

'''
This class is for creating database and table easier by using pymysql
'''

import pymysql
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
        
    def insert_all_TABLE(self,table,value):
        self.cursor.execute('insert into '+table+' values'+value)
        self.conn.commit()
        
    def delete_TABLE(self,table_name):
        self.cursor.execute('drop table if exists '+table_name)
        
    def show_TABLE(self,table_name):
        self.cursor.execute('select * from '+table_name)
        return self.cursor.fetchall()
    
    def show_une(self,table_name,require):
        self.cursor.execute('select U,N,E from '+table_name+' where '+require)
        U=[]
        N=[]
        E=[]
        data=self.cursor.fetchall()
        for i in range(len(data)):
            U.append(data[i][0])
            N.append(data[i][1])
            E.append(data[i][2])
        return U,N,E
        
    def close(self):
        self.cursor.close()
        self.conn.close()
    

if __name__=='__main__':

    db=mysql_data('root','622825')
    db.create_DATABASE('test5')
    db.use_DATABASE('test1')
    db.create_TABLE('hh','id int,name varchar(20) charset utf8')
    db.insert_all_TABLE('hh(id,name)',"(11,'苏打'),(12,'苏打')")
    db.insert_TABLE('hh(id,name)',"12,'sss'")
    print(db.show_DATABASE())
    print(db.show_TABLE('hh'))
    db.delete_TABLE('hh')
    db.close()
