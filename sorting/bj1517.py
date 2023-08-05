#!/usr/bin/env python

import sys
input= sys.stdin.readline

n=int(input())
li=list(map(int,input().split()))

cnt=0

def merge(s,e):
    global cnt,li
    if s<e:
        m = (s+e)//2
        merge(s,m)
        merge(m+1,e)
        tmp=[]

        x,y = s, m+1
        while x<=m and y<=e:
            if li[x]<=li[y]:
                tmp.append(li[x])
                x+=1
            else:
                tmp.append(li[y])
                y+=1
                cnt+=(m-x)+1

        if x<=m:
            tmp += li[x:m+1]
        if y<=e :
            tmp+= li[y:e+1]
        for i in range(len(tmp)):
            li[s+i] = tmp[i]
merge(0,n-1)
print(cnt)
