#!/usr/bin/env python

from itertools import permutations
import sys
input = sys.stdin.readline

n=int(input())
nums=list(map(int,input().split()))

per=permutations(nums,n)

maxx=-1e9

for num in per:
    sum=0
    for i in range(len(num)-1):
        sum+=abs(num[i+1]-num[i])
    maxx=max(maxx,sum)
print(maxx)
