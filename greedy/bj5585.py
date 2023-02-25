#!/usr/bin/env python

m=int(input())
n=1000-m

cnt=0
li=[500,100,50,10,5,1]

for i in li:
    if (n//i !=0): 
        cnt+=n//i
        n=n%i
print(cnt)

