#!/usr/bin/env python

import sys
input =sys.stdin.readline

stu=[]
for i in range(int(input())):
    stu.append(input().split())

stu.sort(key=lambda x : (-int(x[1]),int(x[2]),-int(x[3]),x[0]))

for i in range(len(stu)):
    print(stu[i][0])
