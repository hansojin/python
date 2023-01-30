#!/usr/bin/env python

t=int(input())

for _ in range(t):
    floor=int(input())
    ho=int(input())
    f=[x for x in range(1,ho+1)]

    for k in range(floor):
        for i in range(1,ho):
            f[i]+=f[i-1]
     print(f[-1])
