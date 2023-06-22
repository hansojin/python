#!/usr/bin/env python

import sys
input= sys.stdin.readline

n,m=map(int,input().split())
li=list(map(int,input().split()))
po=[]
ne=[]
maxx=0

for i in li:
    if i>0:
        po.append(i)
    else:
        ne.append(i)

    if abs(i)>abs(maxx):
        maxx=i

po.sort(reverse=True)
ne.sort()
ans=0

for i in range(0,len(po),m):
    if po[i]!=maxx:
        ans+=po[i]

for i in range(0,len(ne),m):
    if ne[i]!=maxx:
        ans+=abs(ne[i])

ans*=2
ans+=abs(maxx)
print(ans)

