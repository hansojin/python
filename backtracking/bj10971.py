#!/usr/bin/env python

from itertools import permutations

n=int(input())
li=[list(map(int,input().split())) for _ in range(n)]
ans=[]
for i in permutations([i for i in range(0,n)],n):
    res= i + (i[0],)
    tmp=0
    for j in range(n):
        cost = li[res[j]][res[j+1]]
        if cost==0:
            break
        tmp+=cost
    ans.append(tmp)
print(min(ans))
