#!/usr/bin/env python

Date,D,Y,T = input().split()
D=int(D[:-1])
Y=int(Y)
H,M = map(int,T.split(":"))
mname = ["January" , "February", "March", "April", "May", "June", 
            "July", "August", "September", "October", "November", "December"]
mnum=[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
if Y%400==0 or(Y%4==0 and Y%100!=0):
    mnum[1]+=1
total = sum(mnum)*24*60
late = mname.index(Date)
now = (sum(mnum[:late])+D-1)*24*60+H*60+M
print(now/total*100)
