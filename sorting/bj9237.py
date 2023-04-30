#!/usr/bin/env python

import sys
input = sys.stdin.readline

n=int(input())
tree=list(map(int,input().split()))
tree.sort(reverse=True)

for i in range(len(tree)):
    tree[i]=tree[i]+i+1

print(max(tree)+1)
