#!/usr/bin/env python

import sys
input = sys.stdin.readline

n=int(input())
ans=0
li,po,ne=[],[],[]

for _ in range(n):
    li.append(int(input()))
cnt=0
for i in li:
    if i>0:
        po.append(i)
    if i<0:
        ne.append(i)
    if i==0:
        cnt+=1
po.sort(reverse=True)
ne.sort()
for _ in range(cnt):
    ne.append(0)

pol,nel=len(po),len(ne)


if po:
    i=0
    while i<pol-1:
        ans+=max(po[i]*po[i+1],po[i]+po[i+1])
        i+=2
    if pol%2==1:
        ans+=po[pol-1]

if ne:
    i=0
    while i<nel-1:
        ans+=max(ne[i]*ne[i+1],ne[i]+ne[i+1])
        i+=2
    if nel%2==1:
        ans+=ne[nel-1]


print(ans)
