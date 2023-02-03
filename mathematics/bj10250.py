#!/usr/bin/env python

import sys
input = sys.stdin.readline

n=int(input())

for _ in range(n):
    h,w,n= map(int,input().split())
    num=n//h+1
    floor = n%h
    if n%h ==0 : 
        num=n//h
        floor = h
    print(f'{floor*100+num}')
