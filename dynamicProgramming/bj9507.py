#!/usr/bin/env python

import sys
input = sys.stdin.readline

li=[1,1,2,4]
for i in range(4,70):
    li.append(li[i-1]+li[i-2]+li[i-3]+li[i-4])
for _ in range(int(input())):
    print(li[int(input())])

