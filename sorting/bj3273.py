#!/usr/bin/env python

import sys
input =sys.stdin.readline

n=int(input())
li=list(map(int,input().split()))
li.sort()
x=int(input())
cnt=0

srt,end=0,n-1
while srt<end:
    tmp=li[srt]+li[end]
    if tmp==x:
        cnt+=1
        srt+=1
        end-=1
    elif tmp<x:
        srt+=1
    else:
        end-=1
print(cnt)
