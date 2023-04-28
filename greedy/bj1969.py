#!/usr/bin/env python

import sys
input =sys.stdin.readline

from collections import Counter

n,m=map(int,input().split())
li=[]
for i in range(n):
    li.append(input())
ans=[]
hd=0
for idx in range(m):
    tmp=[]
    for dna in li:
        tmp.append(dna[idx])
    tmp.sort()
    tmp=Counter(tmp)
    ans.append(tmp.most_common()[0][0])
    hd+=n-tmp.most_common()[0][1]
res=''.join(s for s in ans)
print(res)
print(hd)
    
