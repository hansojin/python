#!/usr/bin/env python

import sys
input = sys.stdin.readline

total = int(input())
for _ in range(int(input())):
    a,b=map(int,input().split())
    total-=a*b

if total==0:
    print('Yes')
else:
    print('No')
