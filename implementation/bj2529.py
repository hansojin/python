#!/usr/bin/env python

n=int(input())
sign=list(input().split())
visit=[0]*10
maxx,minn='',''

def check(i,j,k):
    if k=='<':
        return i<j
    else:
        return i>j
    return True

def solve(cnt,s):
    global maxx,minn
    if cnt==n+1:
        if not len(minn):
            minn=s
        else:
            maxx=s
        return
    for i in range(10):
        if not visit[i]:
            if cnt==0 or check(s[-1],str(i),sign[cnt-1]):
                visit[i]=1
                solve(cnt+1,s+str(i))
                visit[i]=0
solve(0,'')
print(maxx)
print(minn)
