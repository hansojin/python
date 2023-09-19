#!/usr/bin/env python

import sys
input= sys.stdin.readline

n=int(input())
m=int(input())
li,arr=[],[]
s=set()
visit =[False] * n
for _ in range(n):
    li.append(int(input()))

def dfs(cnt):
    if len(arr)==m:
        tmp=''.join(map(str,arr))
        s.add(tmp)
        return
    for i in range(n):
        if visit[i]:
            continue
        visit[i]=True
        arr.append(li[i])
        dfs(cnt+1)
        arr.pop()
        visit[i]=False
dfs(0)
print(len(s))


