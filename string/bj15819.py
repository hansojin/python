#!/usr/bin/env python

a,b=map(int,input().split())
li=[]
for _ in range(a):
    li.append(str(input()))
li.sort()
print(li[b-1])
