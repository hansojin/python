#!/usr/bin/env python


n,m=map(int,input().split())

arr=[]

def dfs(num):
    if len(arr)==m:
        print(*arr)
        return
    for i in range(num,n+1):
        #if i not in arr:
        arr.append(i)
        dfs(i)
        arr.pop()
dfs(1)

