#!/usr/bin/env python

import sys
input = sys.stdin.readline

while(True):
    num=list(map(int,input().split()))
    max_num=max(num)
    if(max_num ==0):
        break
    num.remove(max_num)

    if max_num*max_num==num[0]**2+num[1]**2:
        print('right')
    else:
        print('wrong')


