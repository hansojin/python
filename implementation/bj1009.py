#!/usr/bin/env python

for _ in range(int(input())):
    a,b=map(int,input().split())
    tmp=a**b
    tmp=list(map(int,str(tmp)))
    print(tmp[-1])
