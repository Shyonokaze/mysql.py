#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 15:09:31 2018

@author: pyh
"""    

from mysql_data import *
import numpy as np
import os

dirpath='/home/pyh/0-work/station/'
db_name='data'   
    
db=mysql_data('root','622825')
db.create_DATABASE(db_name)  




for file_name in os.listdir(dirpath):
    table_name=file_name[0:7]

    fid=open(dirpath+file_name,'rt')
    line=fid.readline()
    table_head=list(line.split())[0:-1]
    define_table=''
    using_table=''
    for i in range(len(table_head)):
        define_table=define_table+table_head[i]+' float, '
        using_table=using_table+table_head[i]+', '
    line=fid.readline()
    data=[]
    num=0
    while line:
        data.append([])
        sing=line.split()
        for i in range(len(sing)):
            data[num].append(float(sing[i]))
        num+=1
        line=fid.readline()        
        
    value=''
    for i in range(len(data)):
#    for i in range(100):
        value=value+'('
        sing=''
        for j in range(len(data[0])):
            sing=sing+str(data[i][j])+","        
        value=value+sing[0:-1]+'),'
        
    db.create_TABLE(table_name,define_table[0:-2])
    
    db.insert_all_TABLE(table_name+'('+using_table[0:-2]+')',value[0:-1])
        
    print(db.show_TABLE(table_name))

db.close()
