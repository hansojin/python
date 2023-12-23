#!/usr/bin/env python 

import sys
input= sys.stdin.readline

a,b,c=map(int,input().split())
if b<=a<=c:
    print(a)
else:
    if abs(b-a)<abs(c-a):
        print(b)
    else:
        print()
