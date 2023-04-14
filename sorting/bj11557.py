#!/usr/bin/env python

import sys
input =sys.stdin.readline

for _ in range(int(input())):
    li=[]
    for _ in range(int(input())):
        li.append(input().split())
        li.sort(key= lambda x : -int(x[1]))
    print(li[0][0])

