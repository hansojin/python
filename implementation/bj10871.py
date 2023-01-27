#!/usr/bin/env python

a,b=map(int,input().split())
n_list=list(map(int,input().split()))

for x in range(a):
    if n_list[x]<b:
        print(n_list[x], end=" ")
