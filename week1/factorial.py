#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     factorial.py
   Description :
   Author :        changyy
   date：          2020/4/11 0011 10:21
-------------------------------------------------
   Change Activity:
                   2020/4/11 0011 10:21
-------------------------------------------------
"""
__author__ = 'changyy'

"""
M! / (N! * (M-N)!)
"""


def factorrial(x):
    result = 1
    for i in range(1, x + 1):
        result *= i
    return result


m = int(input('请输入M：'))
n = int(input('请输入N：'))

print(factorrial(m) // factorrial(n) // factorrial(m - n))
