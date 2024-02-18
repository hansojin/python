#!/usr/bin/env python

import sys
input= sys.stdin.readline

n=int(input())
li=list(map(str,input().split()))
hbit=input().rstrip()
print(li.count(hbit))
