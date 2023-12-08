#!/usr/bin/env python

import sys
input= sys.stdin.readline

n=int(input())
m=int(input())

if m==0:
    print(n)
    sys.exit(0)

li=[tuple(map(int,input().split()))
    for _ in range(m)
]

li.sort()

start,end=li[0]
ans=n

for ns, ne in li:
    if end>=ns:
        end=max(end,ne)
    else:
        ans-=(end-start)
        start,end=ns,ne
ans-=(end-start)
print(ans)
