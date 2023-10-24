#!/usr/bin/env python

n=int(input())
li=[[[0] for _ in range(n)] for _ in range(n)]
for i in range(n):
    li[i]=list(map(int,input().split()))

for i in range(1,n):
    for j in range(len(li[i])):
        if j==0:
            li[i][j]=li[i][j]+li[i-1][j]
        elif j==len(li[i])-1:
            li[i][j]=li[i][j]+li[i-1][j-1]
        else:
            li[i][j]=li[i][j]+max(li[i-1][j-1],li[i-1][j])
    
print(max(li[n-1]))
