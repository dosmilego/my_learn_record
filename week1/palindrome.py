#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     palindrome.py.py
   Description :   实现判断一个数是不是回文数的函数
   Author :        changyy
   date：          2020/4/11 0011 18:24
-------------------------------------------------
   Change Activity:
                   2020/4/11 0011 18:24
-------------------------------------------------
"""
__author__ = 'changyy'

"""
设n是一任意自然数。若将n的各位数字反向排列所得自然数n1与n相等，则称n为一回文数
"""


def is_palindrome(x):
    temp = x
    sum = 0
    while temp > 0:
        sum = sum * 10 + temp % 10
        temp = temp // 10
    if sum == x:
        print('%d是回文数' % x)
    else:
        print('%d不是回文数' % x)


if __name__ == '__main__':
    i = int(input('X:'))
    is_palindrome(i)
