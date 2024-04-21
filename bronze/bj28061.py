#!/usr/bin/env python

n=int(input())
li=list(map(int,input().split()))
maxx=-1
for i in range(n):
    tmp=li[i]-(n-i)
    if maxx<tmp:
        maxx=tmp
print(maxx)
