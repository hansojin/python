#!/usr/bin/env python

li=[False,True,False,False]

for _ in range(int(input())):
    a,b=map(int,input().split())
    li[a],li[b]=li[b],li[a]

for i in range(4):
    if li[i]==True:
        print(i)
