#!/usr/bin/env python

import sys
input=sys.stdin.readline

n=int(input())
cnt=0
arr={}
for i in range(n):
    arr[input().rstrip()]=i
for i in range(n):
    c=input().rstrip()
    if next(iter(arr))!=c:
        cnt+=1
    arr.pop(c)
print(cnt)
