#!/usr/bin/env python

import sys
input = sys.stdin.readline

n=int(input())
li=list(map(int,input().split()))
li.sort()
ans=[]
value=10000000000
srt,end=0,n-1

while srt<end:
    tmp=li[srt]+li[end]
    if abs(tmp)<value:
        value=abs(tmp)
        ans=[li[srt],li[end]]
        if tmp==0:
            break
    if tmp<0:
        srt+=1
    else:
        end-=1

print(ans[0],ans[1])
