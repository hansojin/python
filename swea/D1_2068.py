#!/usr/bin/env python

n=int(input())
for i in range(n):
    li=list(map(int,input().split()))
    print(f'#{i+1} {max(li)}')
