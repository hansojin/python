#!/usr/bin/env python

import sys
input= sys.stdin.readline

n=int(input())
li=sorted(list(map(int,input().split())))
print(li[(n-1)//2])
