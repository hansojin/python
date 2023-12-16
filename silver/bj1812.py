#!/usr/bin/env python

import sys
input= sys.stdin.readline

n=int(input())
li=[int(input()) for _ in range(n)]
res=[]
ans=0

for i,v in enumerate(li):
    if i%2==0:
        ans+=v
    else:
        ans-=v
res.append(ans//2)

for i in range(n-1):
    res.append(li[i]-res[i])
for i in res:
    print(i)
