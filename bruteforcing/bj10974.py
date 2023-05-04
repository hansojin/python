#!/usr/bin/env python

import itertools

n=int(input())
arr=[]
for i in range(1,n+1):
    arr.append(i)
ans=itertools.permutations(arr,n)
for i in ans:
    print(*i)
