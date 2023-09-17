#!/usr/bin/env python

a,b,c=map(int,input().split())
d=b*c
ans=a-d
if ans<0:
    print(0,ans+b-1)
else:
    print(ans,ans+b-1)
