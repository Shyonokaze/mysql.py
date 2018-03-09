#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  9 10:15:46 2018

@author: pyh
"""



def cal_u95(u,n,e):
    import numpy as np
    h=[]
    for i in range(len(n)):
        h_value=np.sqrt(n[i]*n[i]+e[i]*e[i])
        h.append(h_value)
    u95=np.percentile(np.array(u[1800:]),95)
    h95=np.percentile(np.array(h[1800:]),95)
    return u95,h95


import os
dirpath='/home/pyh/0-work/station/'

db=mysql_data('root','622825')
db.use_DATABASE('data')
U,N,E=db.show_une('Station',"base_station='chal064'")

u95,h95=cal_u95(U,N,E)
print(u95,h95)
#for file in os.listdir(dirpath):
#    print('%s\t%.2f\t%.2f'%(file,cal_u95(dirpath+file)[0],cal_u95(dirpath+file)[1]))
