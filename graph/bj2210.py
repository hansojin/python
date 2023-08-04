#!/usr/bin/env python
import sys
sys.setrecursionlimit(10**6)

li=[list(map(str,input().split())) for _ in range(5)]
ans = set()

def dfs(i,j,ch):
    if len(ch)==6:
        ans.add(ch)
        return
    if i<0 or j<0 or i>4 or j>4:
        return
    ch+=str(li[i][j])

    dfs(i,j+1,ch)
    dfs(i,j-1,ch)
    dfs(i-1,j,ch)
    dfs(i+1,j,ch)

for i in range(5):
    for j in range(5):
        dfs(i,j,"")

print(len(ans))
