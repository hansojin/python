#!/usr/bin/env python

import sys
input = sys.stdin.readline
from collections import Counter

n,m=map(int,input().split())
li=[]
ans=[]
for _ in range(n+m):
    word=input().rstrip()
    li.append(word)
tmp=Counter(li)
for i in tmp:
    if tmp[i]==2:
        ans.append(i)

ans.sort()
print(len(ans))
for i in range(len(ans)):
    print(ans[i])
