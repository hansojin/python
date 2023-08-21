#!/usr/bin/env python

import sys
input = sys.stdin.readline

p,j=0,0
n=int(input())
li=sorted(list(map(int,input().split())))
p+=sum(li[n//2:])
print(sum(li)-p,p)
