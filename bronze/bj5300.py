#!/usr/bin/env python

import sys
input= sys.stdin.readline

for _ in range(int(input())):
    g,i,e=map(int,input().split())
    r=e-i

    if g==1:
        tmp=r
    elif g==2:
        tmp=r*3
    else:
        tmp=r*5
    if tmp<=0:
        print(0)
    else:
        print(tmp)
