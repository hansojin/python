#!/usr/bin/env python

import itertools

n=int(input())
k=int(input())
num=[]
for _ in range(n):
    num.append(int(input()))

li=itertools.permutations(num,k)
sett=set()
for i in li:
    tmp=(''.join(map(str,i)))
    sett.add(tmp)

print(len(sett))
