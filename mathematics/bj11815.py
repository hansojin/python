#!/usr/bin/env python

import sys
input= sys.stdin.readline
import math

def prime(n):
    dc=dict()
    d,sqrt=2,int(math.sqrt(n))
    while d<=sqrt:
        if n%d!=0:
            d+=1
        else:
            if d in dc:
                dc[d]+=1
            else:
                dc[d]=1
            n//=d
    ans=1
    for i in dc.values():
        ans*=(i+1)
    return ans

cnt = int(input())
num = list(map(int,input().split()))

for i in range(cnt):
    if num[i] == (int(num[i] ** 0.5) ** 2):
        print(1, end = " ")
    else:
        print(0, end = " ")
