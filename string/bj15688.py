#!/usr/bin/env python

import sys
input= sys.stdin.readline

li=[]
for _ in range(int(input())):
    num=int(input())
    li.append(num)

li.sort()
for i in li:
    print(i)
