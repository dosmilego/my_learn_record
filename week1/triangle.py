#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     triangle.py
   Description :
   Author :       changyy
   date：          2020/4/10 0010 17:19
-------------------------------------------------
   Change Activity:
                   2020/4/10 0010 17:19
-------------------------------------------------
"""
__author__ = 'changyy'

row = int(input('请输入行数: '))
for i in range(row):
    for _ in range(i + 1):
        print('*', end='')
    print()


for i in range(row):
    for j in range(row):
        if j < row - i - 1:
            print(' ', end='')
        else:
            print('*', end='')
    print()

for i in range(row):
    for _ in range(row - i - 1):
        print(' ', end='')
    for _ in range(2 * i + 1):
        print('*', end='')
    print()
