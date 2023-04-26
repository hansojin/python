#!/usr/bin/env python

maxx=-1e9
for _ in range(int(input())):
    a,d,g=map(int,input().split())
    total=a*(d+g)
    if d+g==a:
        total*=2
    maxx=max(total,maxx)
print(maxx)
