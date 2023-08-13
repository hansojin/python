#!/usr/bin/env python

import sys
input= sys.stdin.readline

N = int(input())

w = input().split('*')

for _ in range(N):
    word = input()

    if word[:len(w[0])] == w[0] and word[-len(w[1]):] == w[1] and len("".join(w)) <=len(word):
        print("DA")
    else:
        print("NE")
