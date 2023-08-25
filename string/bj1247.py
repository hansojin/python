#!/usr/bin/env python

import sys
input= sys.stdin.readline

for _ in range(3):
    li=[]
    for _ in range(int(input())):
        li.append(int(input()))
    comp=sum(li)
    if comp>0:
        print("+")
    elif comp<0:
        print("-")
    else:
        print(0)
