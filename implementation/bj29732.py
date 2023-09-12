#!/usr/bin/env python

import sys
input= sys.stdin.readline

n,m,k=map(int,input().split())
li=input()
r=[]
for i in range(n):
    if li[i]=='R':
        r.append(i)
rr = [0]*(n+1)

for i in r:
    s= max(0,i-k)
    e = min(n-1,i+k)
    for j in range(min(s,e),max(s,e)+1):
        rr[j]=1
if sum(rr)-rr[-1]<=m:
    print("Yes")
else:
    print("No")

