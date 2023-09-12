#!/usr/bin/env python

MOD = 1000000007

def cal(b, e):
    res = 1
    while e > 0:
        if e % 2 == 1:
            res = (res * b) % MOD
        b = (b * b) % MOD
        e //= 2
    return res

a, b = map(int, input().split())

res = cal(b, a)
sub = cal(b - 1, a)

c = (res - sub) % MOD
print(c)

