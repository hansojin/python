#!/usr/bin/env python

n,m=map(int,input().split())

dp=[ (1,0),(0,1)]

for i in range(2,n):
    dp.append((dp[i-1][0]+dp[i-2][0],dp[i-1][1]+dp[i-2][1]))
    
a=dp[-1][0]
b=dp[-1][1]

ind,dex=1,1
while True:
    if a*ind + b*dex==m:
        print(ind)
        print(dex)
        break
    elif a*ind + b*dex<m:
        dex+=1
    else:
        ind+=1
        dex=1
