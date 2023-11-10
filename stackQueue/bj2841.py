#!/usr/bin/env python

import sys
input= sys.stdin.readline

n,p=map(int,input().split())
li=[[] for _ in range(n+1)]
cnt=0

for _ in range(n):
    a,b=map(int,input().split())
    if li[a]:
        if b>li[a][-1]:
            li[a].append(b)
            cnt+=1
        elif b==li[a][-1]:
            continue
        else:
            while li[a] and b<li[a][-1]:
                li[a].pop()
                cnt+=1
            if li[a] and li[a][-1]==b:
                continue
            li[a].append(b)
            cnt+=1
    else:
        li[a].append(b)
        cnt+=1
print(cnt)
