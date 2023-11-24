#!/usr/bin/env python

import sys
input= sys.stdin.readline

while True:
    n=int(input())
    if n==0:
        break
    li=[]
    maxx=-1
    for i in range(n):
        a,b=input().split()
        b=float(b)
        if b>maxx:
            li=[a]
            maxx=b
        elif b==maxx:
            li.append(a)
    print(*li)
