#!/usr/bin/env python

import sys
input= sys.stdin.readline

word=input().rstrip()

for i in range(len(word)):
    if word[i:]==word[i:][::-1]:
        print(len(word)+i)
        break


