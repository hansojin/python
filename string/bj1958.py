#!/usr/bin/env python

import sys
input = sys.stdin.readline

a=input().strip()
b=input().strip()
c=input().strip()

x,y,z=len(a),len(b),len(c)
arr = [[[0] * (z+1) for _ in range(y+1)] for _ in range(x+1)]

for i in range(1,x+1):
    for j in range(1,y+1):
        for k in range(1,z+1):
            if a[i-1]==b[j-1]and b[j-1]==c[k-1]:
                arr[i][j][k]=arr[i-1][j-1][k-1]+1

            else:
                arr[i][j][k]=max(arr[i][j][k-1], arr[i][j-1][k], arr[i-1][j][k])
ans=-1
for i in range(x+1):
    for j in range(y+1):
        ans=max(max(arr[i][j]),ans)
print(ans)
