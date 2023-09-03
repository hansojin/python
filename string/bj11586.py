#!/usr/bin/env python

import sys
input= sys.stdin.readline

n=int(input())
li=[list(input()) for _ in range(n)]

op= int(input())
if op==1:
    for i in range(n):
        for j in range(n):
            print(li[i][j],end='')
        print()
elif op==3:
    for i in range(n-1,-1,-1):
        for j in range(n):
            print(li[i][j],end='')
        print()
elif op==2:
    for i in range(n):
        for j in range(n-1,-1,-1):
            print(li[i][j],end='')
        print()

