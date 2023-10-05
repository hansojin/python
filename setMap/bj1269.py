#!/usr/bin/env python

import sys
input = sys.stdin.readline

a,b=map(int,input().split())

a_li=set(map(int,input().split()))
b_li=set(map(int,input().split()))

print(len(a_li^b_li))
