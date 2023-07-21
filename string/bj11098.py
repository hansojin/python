#!/usr/bin/env python

import sys
input= sys.stdin.readline

for _ in range(int(input())):
    arr=[]
    for _ in range(int(input())):
        price,name=input().split()
        price=int(price)
        arr.append((price,name))
    arr.sort(key = lambda x : x[0])
    print(arr[-1][1])

