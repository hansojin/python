#!/usr/bin/env python

import sys
input= sys.stdin.readline

while True:
    n,m=map(int,input().split())
    if n==m==0:
        break
    li=[]
    dummy=''
    for _ in range(m+2):
        dummy+='.'
    li.append(dummy)
    for _ in range(n):
        li.append('.'+input().rstrip()+'.')
    li.append(dummy)
    for i in range(1,1+n):
        ans=''
        for j in range(1,1+m):
            if li[i][j]=='*':
                ans+=('*')
            else:
                cnt=0
                for x in range(i-1,i+2):
                    for y in range(j-1,j+2):
                        if x==i and y==j:
                            continue
                        if li[x][y]=='*':
                            cnt+=1
                ans+=str(cnt)
        print(ans)


                
