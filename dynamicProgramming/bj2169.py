#!/usr/bin/env python

import sys
input= sys.stdin.readline

n,m=map(int,input().split())
li=[list(map(int,input().split())) for _ in range(n)]

for j in range(1,m):
    li[0][j]+=li[0][j-1]

for i in range(1,n):
    left = [li[i][j]+li[i-1][j] for j in range(m)]
    right = [li[i][j]+li[i-1][j] for j in range(m)]

    for j in range(1,m):
        left[j]=max(left[j],left[j-1]+li[i][j])
    for j in range(m-2,-1,-1):
        right[j]=max(right[j],right[j+1]+li[i][j])

    for j in range(m):
        li[i][j]=max(left[j],right[j])
print(li[-1][-1])
