#!/usr/bin/env python   
a,b=map(int,input().split())
num=1
li=[0]*1000
for i in range(1,60):
    ind=i
    while ind>0:
        li[num]=i
        num+=1
        ind-=1
summ=0
for i in range(a,b+1):
    summ+=li[i]
print(summ)
