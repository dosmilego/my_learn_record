#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     shuixianhua.py
   Description :
   Author :       changyy
   date：          2020/4/10 0010 17:41
-------------------------------------------------
   Change Activity:
                   2020/4/10 0010 17:41
-------------------------------------------------
"""
__author__ = 'changyy'

for numbers in range(100, 1000):
    a = numbers // 100
    b = numbers // 10 % 10
    c = numbers % 10
    if numbers == a ** 3 + b ** 3 + c ** 3:
        print(numbers)
