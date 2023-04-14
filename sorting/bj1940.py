#!/usr/bin/env python

import sys
input =sys.stdin.readline

n=int(input())
m=int(input())
num=list(map(int,input().split()))
num.sort()

srt,end=0,1
cnt=0
mm=num[srt]+num[end]

while srt<end:
    if mm>m:
        break
    if mm==m:
        cnt+=1
        srt+=1
        end=srt+1
        mm=num[srt]+num[end]

    elif end==n:
        mm-=num[srt]
        srt+=1
        mm+=num[srt]
    else:
        mm-=num[end]
        end+=1
        mm+=num[end]
    print(srt,end)
print(cnt)

