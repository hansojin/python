#!/usr/bin/env python

import sys
input= sys.stdin.readline

n=int(input())
paper = [list(map(int, input().split())) for _ in range(n)]
res={-1:0,0:0,1:0}

def solution(x, y, n) :
    color = paper[x][y]
    for i in range(x, x+n) :
        for j in range(y, y+n) :
            if color != paper[i][j] :
                nxt=n//3
                solution(x, y, nxt)
                solution(x, y+nxt, nxt)
                solution(x,y+(nxt*2),nxt)
                solution(x+nxt, y, nxt)
                solution(x+nxt,y+nxt,nxt)
                solution(x+nxt,y+(nxt*2),nxt)
                solution(x+(nxt*2), y, nxt)
                solution(x+(nxt*2), y+nxt, nxt)
                solution(x+(nxt*2), y+(nxt*2), nxt)
                return
    res[color]+=1
    return


solution(0,0,n)
for i in res.values():
    print(i)

