#!/usr/bin/env python

import sys
input= sys.stdin.readline

n=int(input())
li=[]
for _ in range(n):
    a,b=map(int,input().split())
    li.append([a,b])
li.sort(key = lambda x:x[0])

ans=0
for i in range(len(li)):
    if ans<li[i][0]:
        ans=li[i][0]+li[i][1]
    else:
        ans+=li[i][1]
print(ans)
