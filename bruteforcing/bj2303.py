#!/usr/bin/env python

from itertools import combinations

n=int(input())
ans=[]

for i in range(n):
    num = list(combinations(list(map(int,input().split())),3))
    score= 0
    for n in num:
        tmp= sum(n)%10
        score = max(score, tmp)
    ans.append((score,i+1))
ans = sorted(ans, key = lambda x : (-x[0], -x[1]))
print(ans[0][1])
