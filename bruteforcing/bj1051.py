#!/usr/bin/env python

import sys
input= sys.stdin.readline

n,m=map(int,input().split())
li=[]
for _ in range(n):
    li.append(list(input()))

check=min(n,m)
ans=0

for i in range(n):
    for j in range(m):
        for k in range(check):
            if ((i + k) < n) and ((j + k) < m) and (li[i][j] == li[i][j + k] == li[i + k][j] == li[i + k][j + k]):
                ans = max(ans, (k + 1)**2)
print(ans)
