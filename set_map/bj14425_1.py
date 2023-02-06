#!/usr/bin/env python

n,m=map(int,input().split())
s=[]

for _ in range(n):
    s.append(str(input()))

sset=set(s)
cnt=0

for i in range(m):
    mstr=str(input())
    if mstr in sset:
        cnt+=1
print(cnt)
