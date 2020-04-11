#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     gcd_lcm.py
   Description :   求两个数的最大公约数和最小公倍数
   Author :        changyy
   date：          2020/4/11 0011 11:34
-------------------------------------------------
   Change Activity:
                   2020/4/11 0011 11:34
-------------------------------------------------
"""
__author__ = 'changyy'

"""
两个数a, b
最大公约数[a, b],最小公倍数(a, b)
存在数学定理:a * b = [a, b] * (a, b)
"""


def gcd(a, b):
    # 计算最大公约数,最大公约数不会大于两个数中较小的那个数
    (a, b) = (b, a) if a > b else (a, b)
    for factor in range(a, 0, -1):
        if a % factor == 0 and b % factor == 0:
            return factor


def lcm(a, b):
    # 计算最小公倍数
    return a * b // gcd(a, b)


if __name__ == '__main__':
    x = int(input('X:'))
    y = int(input('Y:'))
    print('最大公约数:%d' % gcd(x, y))
    print('最小公倍数:%d' % lcm(x, y))
