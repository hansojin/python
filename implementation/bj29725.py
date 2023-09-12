#!/usr/bin/env python

dic = {'.':0 , 'K':0, 'k':0, 'P':1, 'p':-1, 'N':3, 'n':-3, 'B':3, 'b':-3, 'R':5, 'r':-5, 'Q':9, 'q':-9}

chess = []
for _ in range(8):
    chess.append(input())

ans=0
for i in range(8):
    for j in range(8):
        ans+=dic[chess[i][j]]
print(ans)
