#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 11:13:35 2018

@author: pyh
"""
import xlrd
sheet=xlrd.open_workbook('基准站配置0305.xlsx')
table_head=['lb','lbxh','zddh','zdmc','jsjIP','ckzbh','jsjbh','txbh','txxh',
            'jsjpp','jsjxh','ssq','dw','zdszfwq','zdszgc','sjbfdk','nwbfdk',
            'gcdlx','sjcsgs','yys','cslx','zdjrsj','dz','kjzdmc','zdbh',
            'gcz','wdyzz','yzz','hxzd','jsjwldlyhm','jsjwydlmm','bz']
date_table_head=['zdjrsj']
