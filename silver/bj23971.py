#!/usr/bin/env python

h,w,n,m=map(int,input().split())
r=ceil(h/(n+1))
c=ceil(w/(m+1))
print(r*c)
