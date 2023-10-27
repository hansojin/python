#!/usr/bin/env python

import sys
input= sys.stdin.readline

b,c,d=map(int,input().split())
sets=min(b,c,d)

burger=sorted(list(map(int,input().split())),reverse=True)
side = sorted(list(map(int,input().split())),reverse=True)
drinks=sorted(list(map(int,input().split())),reverse=True)

total = sum(burger) + sum(side) + sum(drinks)
tmp = sum(burger[:sets]) + sum(side[:sets]) + sum(drinks[:sets])
print(total)
print(total - tmp//10)
