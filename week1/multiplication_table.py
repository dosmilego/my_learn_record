#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     chengfabiao.py
   Description :   九九乘法表
   Author :        changyy
   date：          2020/4/10 0010 16:35
-------------------------------------------------
   Change Activity:
                   2020/4/10 0010 16:35
-------------------------------------------------
"""

__author__ = 'changyy'


for m in range(1, 10):
    for n in range(1, m + 1):
        print('%d * %d = %d' % (n, m, n * m), end='\t')
    print()
