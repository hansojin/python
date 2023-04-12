#!/usr/bin/env python

import sys
input = sys.stdin.readline

n,m=map(int,input().split())
li=list(map(int,input().split()))

srt=0
end=0
ans=100000
summ=0
while srt<n:
    #print(srt,end)
    if summ>m:
        if end-srt<ans:
            if srt==0:
                ans=end-srt+1
            else:
                ans=end-srt
        summ-=li[srt]
        srt+=1
    else:
        summ+=li[end]
        if end<n-1:
            end+=1
        else:
            break
    #print(summ,ans)
    #print()


if ans==100000:
    print(0)
else:
    print(ans)
    
