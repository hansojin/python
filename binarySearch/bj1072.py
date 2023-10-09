#!/usr/bin/env python

import sys
input= sys.stdin.readline

x,y=map(int,input().split())
z=(y*100)//x

if z>=99:
    print(-1)
else:
    ans=0
    s,e=1,x

    while s<=e:
        mid=(s+e)//2
        if (y+mid)*100 // (x+mid)<=z:
            s=mid+1
        else:
            ans=mid
            e=mid-1
    print(ans)
