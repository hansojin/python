#!/usr/bin/env python

import sys
input= sys.stdin.readline

n=int(input())
day=[0]
li=[[] for _ in range(n+1)]
for i in range(n):
    tmp=list(map(int,input().split()))
    day.append(tmp[0])
    if len(tmp)!=2:
        li[i+1]=tmp[1:-1]
for i in range(1,n+1):
    ans=day[i]
    s=set()
    if li[i]:
        for d in li[i]:
            s.add(d)
            if li[d]:
                for i in range(len(li[d])):
                    s.add(li[d][i])
        for d in s:
            ans+=day[d]
    print(ans)    
    

