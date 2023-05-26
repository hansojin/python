#!/usr/bin/env python

import sys
input= sys.stdin.readline

li=[]
n,m=map(int,input().split())
for _ in range(n):
    word=input().rstrip()
    li.append(word[::-1])
for i in li:
    print(i)
