#!/usr/bin/env python

import sys
input = sys.stdin.readline

n=int(input())
li=list(map(int,input().split()))
li.sort()
print(li[0]*li[n-1])
#print(li[0]*li[-1])
