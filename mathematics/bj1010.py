#!/usr/bin/env python

import math

n=int(input())

for _ in range(n):
    a,b=map(int,input().split())

    ans = math.factorial(b)//(math.factorial(a) * math.factorial(b-a))
    print(ans)

