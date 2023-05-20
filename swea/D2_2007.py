#!/usr/bin/env python

cases=int(input())
for case in range(cases):
    p=str(input())
    for i in range(1,10):
        if p[:i]==p[i:i*2]:
            print(f'#{case+1} {i}')
            break
