#!/usr/bin/env python

import sys
input= sys.stdin.readline

for _ in range(int(input())):
    cry=list(map(str,input().split()))
    while True:
        a=input().split()
        if a[0]=='what':
            print(*cry)
            break
        else:
            remove={a[2]}
            cry=[i for i in cry if i not in remove]


