# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
class mysql_data:
    def __init__(self,user_name,password):
        self.conn=pymysql.connect(host='127.0.0.1',
                 port=3306,
                 user=user_name,
                 passwd=password)
        self.cursor=self.conn.cursor()
        
    def create_DATABASE(self,db_name):
        self.cursor.execute('drop database if exists '+db_name)
        self.cursor.execute('create database '+db_name)
        self.cursor.execute('use '+db_name)
        
#    def delete_DATABASE(self,db_name):
#        self.cursor.execute('drop database if exists '+db_name)

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
    

import pymysql
db=mysql_data('root','622825')
db.create_DATABASE('test5')
db.use_DATABASE('test2')
db.create_TABLE('uu','id int,name varchar(20)')
db.insert_TABLE('uu(id,name)',"11,'aaa'")
db.insert_TABLE('uu(id,name)',"12,'bbb'")
print(db.show_DATABASE())
print(db.show_TABLE('uu'))
db.delete_TABLE('uu')
db.close()
