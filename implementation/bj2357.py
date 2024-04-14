#!/usr/bin/env python

import sys
input= sys.stdin.readline
sys.setrecursionlimit(10**6)
INF = sys.maxsize

N, M = map(int, input().split())
data = [0] + [int(input()) for _ in range(N)]
treeMin = [0] * (N*4)
treeMax = [0] * (N*4)

def initMin(start, end, index):
    if start == end:
        treeMin[index] = data[start]
        return treeMin[index]

    mid = (start+end)//2
    treeMin[index] = min(initMin(start, mid, index*2), initMin(mid+1, end, index*2+1))
    return treeMin[index]

def initMax(start, end, index):
    if start == end:
        treeMax[index] = data[start]
        return treeMax[index]

    mid = (start+end)//2
    treeMax[index] = max(initMax(start, mid, index*2), initMax(mid+1, end, index*2+1))
    return treeMax[index]


def findMin(start, end, index, left, right):
    if left > end or right < start:
        return INF

    if left <= start and end <= right:
        return treeMin[index]

    mid = (start+end)//2
    return min(findMin(start, mid, index*2, left, right), findMin(mid+1, end, index*2+1, left, right))

def findMax(start, end, index, left, right):
    if left > end or right < start:
        return 0

    if left <= start and end <= right:
        return treeMax[index]

    mid = (start+end)//2
    return max(findMax(start, mid, index*2, left, right), findMax(mid+1, end, index*2+1, left, right))


initMin(1, N, 1)
initMax(1, N, 1)
for _ in range(M):
    a, b = map(int, input().split())
    print(findMin(1, N, 1, a, b),findMax(1, N, 1, a, b))

