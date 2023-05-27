#!/usr/bin/env python
import sys
input= sys.stdin.readline

n=int(input())
paper = [list(map(int, input().split())) for _ in range(n)] 
w,b=0,0

def solution(x, y, n) :
    global w,b
    color = paper[x][y]
    for i in range(x, x+n) :
        for j in range(y, y+n) :
            if color != paper[i][j] :
                solution(x, y, n//2)
                solution(x, y+n//2, n//2)
                solution(x+n//2, y, n//2)
                solution(x+n//2, y+n//2, n//2)
                return
    if color == 0 :
        w+=1
    else :
        b+=1


solution(0,0,n)
print(w)
print(b)
