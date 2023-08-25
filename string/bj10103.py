#!/usr/bin/env python

import sys
input= sys.stdin.readline

a,b=100,100
for _ in range(int(input())):
    x,y=map(int,input().split())
    if x<y:
        a-=y
    elif x>y:
        b-=x
print(a)
print(b)
