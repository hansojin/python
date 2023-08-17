#!/usr/bin/env python

for i in range(3):
    play = list(map(int,input().split()))
    u = play.count(1)
    if u==1:
        print('C')
    elif u==2:
        print("B")
    elif u==3:
        print("A")
    elif u==4:
        print('E')
    else:
        print("D")
