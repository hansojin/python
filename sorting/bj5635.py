#!/usr/bin/env python

import sys
input =sys.stdin.readline

li=[]
for _ in range(int(input())):
    li.append(input().split())

li.sort(key=lambda x : (int(x[3]),int(x[2]),int(x[1])))
print(li[-1][0])
print(li[0][0])

