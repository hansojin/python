#!/usr/bin/env python

import sys
input= sys.stdin.readline
sys.setrecursionlimit(10 ** 6)
m,n=map(int,input().split())
li=[]
for _ in range(n):
    tmp = input().strip()
    li.append(tmp)

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def DFS(x, y):
    if x < 0 or x >= n or y < 0 or y >= m:
        return False

    if li[x][y] == "*":
        global count
        count += 1
        li[x][y] = "."
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            DFS(nx, ny)
        return True
    return False


count = 0
result = 0

for i in range(n):
    for j in range(m):
        if DFS(i, j) == True:
            num.append(count)
            result += 1
            count = 0

num.sort()
print(result)
for i in range(len(num)):
    print(num[i])
