#!/usr/bin/env python

import sys
input = sys.stdin.readline

n,m=map(int,input().split())
li=list(map(int,input().split()))

srt=0
end=0
ans=100000
summ=0

while srt<=end:
    if summ>=m:
        if end-srt<ans:
            ans=end-srt
        summ-=li[srt]
        srt+=1
    elif end==n:
        break
    else:
        summ+=li[end]
        end+=1

if ans==100000:
    print(0)
else:
    print(ans)
    
