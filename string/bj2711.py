#!/usr/bin/env python

import sys
input= sys.stdin.readline

for _ in range(int(input())):
    n,word=map(str,input().split())
    n=int(n)
    print(word[:n-1]+word[n:])
