#!/usr/bin/env python

news=input()
li=[list(map(str,input())) for _ in range(2)]


ret = [[0]*2 for _ in range(2)]

for r in range(2):
    for c in range(2):
        if news=="E":
            x,y=c,1-r
        elif news=="N":
            x,y=1-r,1-c
        elif news=="W":
            x,y=1-c,r
        else:
            x,y=r,c

        ret[x][y]=li[r][c]


if ret==[['.','O'],['P','.']]:
    print("T")
elif ret==[['I','.'],['.','P']]:
    print("F")
elif ret==[['O','.'],['.','P']]:
    print("Lz")
else:
    print("?")



