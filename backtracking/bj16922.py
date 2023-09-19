#!/usr/bin/env python

from itertools import combinations_with_replacement

n=int(input())
s=set()

for i in combinations_with_replacement([1,5,10,50],n):
    s.add(sum(i))
print(len(s))

