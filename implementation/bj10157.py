#!/usr/bin/env python

c,r = map(int,input().split())
t = int(input())

if t > c*r :
    print(0)
    exit()

dx = [0,1,0,-1]
dy = [-1,0,1,0]

li = [[0]*c for _ in range(r)]
drct = x= y = 0

for seat in range(1,c*r+1) :
    if seat == t:
        print(y+1,x+1)
        break
    else :
        li[x][y] = seat
        x += dx[drct]
        y += dy[drct]

        if x<0 or y<0 or x>=r or y>=c or li[x][y]:
            x -= dx[drct]
            y -= dy[drct]
            drct = (drct+1)%4
            x += dx[drct]
            y += dy[drct]
