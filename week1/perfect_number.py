#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     perfect_number.py
   Description :   找出10000以内的完美数
   Author :        changyy
   date：          2020/4/11 0011 00:01
-------------------------------------------------
   Change Activity:
                   2020/4/11 0011 00:01
-------------------------------------------------
"""
__author__ = 'changyy'

"""
说明：完美数又称为完全数或完备数
它的所有的真因子（即除了自身以外的因子）的和（即因子函数）恰好等于它本身。例如：6（$6=1+2+3$）。
"""
import time

start = time.clock()
for numbers in range(1, 10000):
    result = 0
    for i in range(1, int(numbers / 2) + 1):
        if numbers % i == 0:
            result += i

    if result == numbers:
        print(numbers)
end = time.clock()
print("final is in ", end-start)
