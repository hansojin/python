#!/usr/bin/env python

n=int(input())
m=int(input())
li=list(map(int,input().split()))
if sum(li)>=n:
    print('Padaeng_i Happy')
else:
    print('Padaeng_i Cry')
