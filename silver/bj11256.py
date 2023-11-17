#!/usr/bin/env python

import sys
input= sys.stdin.readline

for _ in range(int(input())):
    x,y=map(int,input().split())
    li=[]
    for _ in range(y):
        a,b=map(int,input().split())
        li.append(a*b)
    li.sort(reverse=True)
    cnt=0
    for i in range(y):
        if sum(li[:i])>=x:
            printi)
            break

