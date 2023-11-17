#!/usr/bin/env python

n, m = map(int, input().split())
if n == 0 :
    print(0)
else :
    li = list(map(int, input().split()))
    tar = 0
    res = 1
    for i in range(n-1, -1, -1) :
        tar += li[i]
        if tar > m :
            res += 1
            tar = li[i]

    print(res)

