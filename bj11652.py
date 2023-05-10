#!/usr/bin/env python
import sys
input = sys.stdin.readline

import collections

li=[]
for _ in range(int(input())):
    num=int(input())
    li.append(num)
li.sort()
print(collections.Counter(li).most_common(1)[0][0])

