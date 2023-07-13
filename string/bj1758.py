#!/usr/bin/env python

import sys
input= sys.stdin.readline

li=[]
for i in range(int(input())):
    n=int(input())
    li.append(n)
li.sort(reverse=True)
ans=0
for i in range(len(li)):
    tmp=li[i]-i
    if tmp>=0:
        ans+=tmp
    
print(ans)
