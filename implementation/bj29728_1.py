#!/usr/bin/env python

import math
n = int(input())
if n > 1:
    arr = [True for i in range(n + 1)]

    for i in range(2, int(math.sqrt(n)) + 1):
        if arr[i] == True:
            j = 2
            while i * j <= n:
                arr[i * j] = False
                j += 1

    prime = []
    for i in range(2, n + 1):
        if arr[i]:
            prime.append(i)
    A = []
    for i in range(1, n + 1):
        if i in prime:
            if len(A) > 0 and A[-1] == 'B':
                A[-1] = 'S'
                A.append('S')
            else:
                A.append('S')
                A.reverse()
        else:
            A.append('B')
    bcnt = A.count('B')
    print(bcnt, len(A) - bcnt)
else:
    print(1, 0)

