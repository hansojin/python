#!/usr/bin/env python

import sys
input= sys.stdin.readline
li=[]
for _ in range(int(input())):
    name=input().rstrip()
    if len(name)==3:
        li.append(name)
li.sort()
print(li[0])
