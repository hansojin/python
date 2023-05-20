#!/usr/bin/env python

for _ in range(int(input())):
    li=list(map(str,input().split()))
    for i in li:
        print(i[::-1],end=' ')
