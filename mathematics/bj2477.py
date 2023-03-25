#!/usr/bin/env python

s=[] #input
x=[]
y=[]
sq=[]   #뺄 사각형

n=int(input())
for i in range(6):
    way,dist=map(int,input().split())
    s.append([way,dist])

    if s[i][0]==3 or s[i][0]==4:
        y.append(s[i][1])
    if s[i][0]==1 or s[i][0]==2:
        x.append(s[i][1])

for i in range(6):
    if s[i][0]==s[(i+2)%6][0]:  #하나 띤 index끼리 같으면, ㄱㄴ모양의 안쪽
        sq.append(s[(i+1)%6][1])
print(((max(x)*max(y)) - (sq[0]*sq[1]))*n)





