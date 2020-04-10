#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     baiqianbaiji.py
   Description :
   Author :        changyy
   date：          2020/4/10 0010 23:34
-------------------------------------------------
   Change Activity:
                   2020/4/10 0010 23:34
-------------------------------------------------
"""
__author__ = 'changyy'

for a in range(20):
    for b in range(33):
        c = 100 - a - b
        if 5 * a + 3 * b + c / 3 == 100:
            print('公鸡：%d只，母鸡：%d只，小鸡：%d只' % (a, b, c))
