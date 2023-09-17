#!/usr/bin/env python

li=[0]*1000001
for _ in range(int(input())):
    order = list(map(int,input().split()))
    if order[0]==1:
        li[order[2]]=order[1]
    else:
        print(li[order[1]])

