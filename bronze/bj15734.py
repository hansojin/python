#!/usr/bin/env python

l,r,a=map(int,input().split())
while a>0:
    if l>=r:
        a-=1
        r+=1
    else:
        a-=1
        l+=1
print(min(l,r)*2)
