#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     caishuzi.py
   Description :
   Author :       changyy
   date：          2020/4/10 0010 16:23
-------------------------------------------------
   Change Activity:
                   2020/4/10 0010 16:23
-------------------------------------------------
"""
__author__ = 'changyy'

import random

count = 0
number = random.randint(1, 100)
while True:
    count += 1
    a = int(input('请输入:'))
    if a > number:
        print('大一点！')
    elif a < number:
        print('小一点！')
    else:
        print('恭喜你猜对了！！！')
        break
print('您总共猜了%s次' % count)
if count > 7:
    print('您的智商余额严重不足，请充值~ https://www.wobushishax.com/index/')
