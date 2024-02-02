#!/usr/bin/env python

import sys
input= sys.stdin.readline

n = int(input())
li = [list(map(int, input().rstrip())) for _ in range(n)]


def sol(x, y, n):
    num = li[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if num != li[i][j]:
                num = -1
                break

    if num == -1:
        print("(", end='')
        n = n // 2
        sol(x, y, n)  
        sol(x, y + n, n)  
        sol(x + n, y, n)
        sol(x + n, y + n, n)  
        print(")", end='')

    elif num == 1:
        print(1, end='')
    else:
        print(0, end='')


sol(0, 0, n)
