#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     prime_numbers.py
   Description :   输出100以内所有的素数
   Author :        changyy
   date：          2020/4/11 0011 00:55
-------------------------------------------------
   Change Activity:
                   2020/4/11 0011 00:55
-------------------------------------------------
"""
__author__ = 'changyy'

"""
说明：素数指的是只能被1和自身整除的正整数（不包括1）。
"""

for i in range(2, 101):
    tag = True
    for j in range(2, int(i / 2) + 1):
        if i % j == 0:
            tag = False
            break
    if tag:
        print(i, end=' ')
