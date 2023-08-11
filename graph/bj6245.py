#!/usr/bin/env python

import sys
input= sys.stdin.readline
from collections import deque

n=int(input())
c={'A':1, 'T':10 , 'J':11, 'Q':12, 'K':13,
   '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}

li=[list(map(str,input().split())) for _ in range(n)]
for i in range(n):
    for j in range(n):
        li[i][j]=c[li[i][j][0]]
        
for i in range(n//2):
    li[i],li[n-i-1]=li[n-i-1],li[i]

ans=[[0]*n for _ in range(n)]
ans[0][0]=li[0][0]

def cost(li,i,j,ans):
    if i==0 and j==0:
        return ans[0][0]
    elif i==0:
        ans[i][j]=ans[0][j-1]+li[0][j]
    elif j==0:
        ans[i][j]=ans[i-1][0]+li[i][0]
    else:
        ans[i][j]=max(ans[i-1][j], ans[i][j-1])+li[i][j]


for i in range(n):
    for j in range(n):
        cost(li,i,j,ans)

print(ans[-1][-1])

