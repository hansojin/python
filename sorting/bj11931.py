#!/usr/bin/env python

import sys
input = sys.stdin.readline

li=[]
for _ in range(int(input())):
    num=int(input())
    li.append(num)
li.sort(reverse=True)
for i in li:
    print(i)
