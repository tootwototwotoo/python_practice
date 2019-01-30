# -*- coding: utf-8 -*-
# @Author: luanminjie
# @Date:   2019-01-29 22:08:05
# @Last Modified by:   luanminjie
# @Last Modified time: 2019-01-29 22:08:05
# 使用二分法计算平方根

import sys

def rooting(number,precision):
    '''
    number , 被开方数
    precision , 精度
    '''
    wx = 1 / 10**precision
    upper = number
    lower = 0
    xjbc = number / 2
    while(abs(xjbc**2 - number) > wx):
        difference = xjbc**2 - number;
        if difference > 0:
            upper = xjbc
        elif difference <0:
            lower = xjbc
        xjbc = (upper + lower) /2
    return round( xjbc,precision)

print(rooting(int(sys.argv[1]),int(sys.argv[2])))
