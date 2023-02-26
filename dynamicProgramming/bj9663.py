#!/usr/bin/env python

n=int(input())
row=[0]*n
visit=[False]*n
cnt=0

def promising(x):
    for i in range(x):
        if row[x]==row[i] or abs(row[x]-row[i])==abs(x-i):
            return False
    return True

def dp(x):
    
    global cnt
    if x==n:
        cnt+=1

    else:
        for i in range(n):
            if visit[i]:
                continue
            row[x]=i

            if promising(x):
                visit[i]=True
                dp(x+1)
                visit[i]=False

dp(0)
print(cnt)
