#!/usr/bin/env python

import sys
input =sys.stdin.readline

n=int(input())
m=int(input())
num=list(map(int,input().split()))
num.sort()

srt,end=0,n-1
cnt=0

while srt<end:
    if num[srt]+num[end]==m:
        cnt+=1
        srt+=1
        end-=1
    elif num[srt]+num[end]<m:
        srt+=1
    else:
        end-=1
print(cnt)

