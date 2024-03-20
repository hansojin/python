#!/usr/bin/env python

import sys
input= sys.stdin.readline

a,b,c,d=map(int,input().split())
li=[list(input()) for _ in range(a)]

for i in range(a):
    for _ in range(c):
        for j in range(b):
            for _ in range(d):
                print(li[i][j],end='')
        print()
