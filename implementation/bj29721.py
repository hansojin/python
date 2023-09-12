#!/usr/bin/env python

import sys
input= sys.stdin.readline

n,k=map(int,input().split())
li= [[0]*n for _ in range(n)]

dx=[-2,2,0,0]
dy=[0,0,-2,2]

for _ in range(k):
    a,b=map(int,input().split())
    x,y=a-1,b-1
    li[x][y]=10

for x in range(n):
    for y in range(n):
        if li[x][y] == 10:
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < n and 0 <= ny < n and li[nx][ny] != 10:
                    li[nx][ny] = 1

cnt=0
for i in li:
    cnt+=sum(i)
print(cnt-k*10)   
