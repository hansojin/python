#!/usr/bin/env python

import sys
input= sys.stdin.readline
sys.setrecursionlimit(100000)

n, m = map(int, input().split())
li = [[]]
for i in range(n):
    li.append(list(map(int, input().split()))[1:])
    
task = [0] * (m+1)

def dfs(x):
    if visit[x]:
        return False
    
    visit[x] = 1
    
    for i in li[x]:
        if task[i] == 0 or dfs(task[i]):
            task[i] = x
            return True

    return False

cnt = 0
for i in range(2):
    for j in range(1, n+1):
        visit = [0] * (n+1)
        if dfs(j):
            cnt += 1


print(cnt)
