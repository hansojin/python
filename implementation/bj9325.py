#!/usr/bin/env python

for _ in range(int(input())):
    s = int(input())
    n = int(input())
    ans = s

    for _ in range(n):
        q, p = map(int, input().split())
        ans += q * p

    print(ans)
