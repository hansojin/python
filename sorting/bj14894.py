#!/usr/bin/env python

import sys
input= sys.stdin.readline

n=int(input())
li=list(map(int,input().split()))
cnt=0
def quick(li):
    global cnt
    if len(li)<=1:
        cnt+=1
        return li
    else:
        cnt+=2
    pivot = li[0]
    tail = li[1:]

    left = [ x for x in tail if x<=pivot]
    right = [ x for x in tail if x>pivot]

    return quick(left) + [pivot] + quick(right)

quick(li)
print(cnt)
