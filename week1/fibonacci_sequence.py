#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     fibonacci_sequence.py
   Description :
   Author :        changyy
   date：          2020/4/10 0010 23:58
-------------------------------------------------
   Change Activity:
                   2020/4/10 0010 23:58
-------------------------------------------------
"""
__author__ = 'changyy'

"""
说明：斐波那契数列（Fibonacci sequence）。
斐波那契数列的特点是数列的前两个数都是1，从第三个数开始，每个数都是它前面两个数的和。
"""

L = [1, 1]
while len(L) < 20:
    L.append(L[-1] + L[-2])
print(L)
