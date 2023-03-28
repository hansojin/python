#!/usr/bin/env python

n=int(input())
k=int(input())

srt,end=1,k

while srt<=end:
    mid=(srt+end)//2
    tmp=0
    for i in range(1,n+1):
        tmp+=min(mid//i,n)

    if tmp>=k:
        ans=mid
        end=mid-1
    else:
        srt=mid+1
print(ans)
