#!/usr/bin/env python

for _ in range(int(input())):
    n=int(input())
    tmp=list(map(str,input().split()))
    tmp=sorted(tmp)
    for i in tmp:
        print(i,end='')
