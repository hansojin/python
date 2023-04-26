#!/usr/bin/env python

n=int(input())
num=list(map(int,input().split()))
op=list(map(int,input().split()))

maxx=-1e9
minn=1e9

def dfs(d,total,plus,minus,mul,div):
    global maxx,minn
    if d==n:
        maxx=max(maxx,total)
        minn=min(minn,total)
    if plus:
        dfs(d+1,total+num[d],plus-1,minus,mul,div)
    if minus:
        dfs(d+1,total-num[d],plus,minus-1,mul,div)
    if mul:
        dfs(d+1,total*num[d],plus,minus,mul-1,div)
    if div:
        dfs(d+1,int(total/num[d]),plus,minus,mul,div-1)

dfs(1,num[0],op[0],op[1],op[2],op[3])
print(maxx)
print(minn)



