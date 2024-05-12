#!/usr/bin/env python

s = int(input())
length = (4*s)-3
arr = [[' ']*(length) for _ in range(length)]

def star(n, x, y):
    global arr
    length = (4*n)-3
    if length == 1:
        arr[x][y] = "*"
        return
    else:
        for i in range(length):
            arr[x][y+i] = "*"
            arr[y+i][x] = "*"
            arr[x+(length-1)][y+i] = "*"
            arr[x+i][y+(length-1)] = "*"
        n,x,y = n-1,x+2,y+2
        star(n, x, y)
        return

star(s, 0, 0)
for i in range(length):
    print(*arr[i], sep = '')

