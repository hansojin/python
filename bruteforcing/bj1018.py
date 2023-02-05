'''
 문제 이해를 잘못함
 맨 왼쪽 위칸의 기준이 입력받은 arr가 아니라
 내가 선택한 8*8 체스판 기준임
''' 

#!/usr/bin/env python

import sys
input = sys.stdin.readline

a,b=map(int,input().split())

arr = []
for i in range(a):
    arr.append(list(str(input())))


w_li=[]
for i in range(a//2+1):
    w_li.append(list(str('WB'*((b+1)//2))))
    w_li.append(list(str('BW'*((b+1)//2))))

b_li = []
for i in range(a//2+1):
    b_li.append(list(str('BW'*((b+1)//2))))
    b_li.append(list(str('WB'*((b+1)//2))))


comp=[[0 for _ in range(b)] for __ in range(a)]

if arr[0][0]=='W':
    for i in range(a):
        for j in range(b):
            if arr[i][j]!=w_li[i][j]:
                comp[i][j]=1

elif arr[0][0]=='B':
    for i in range(a):
        for j in range(b):
            if arr[i][j]!=b_li[i][j]:
                comp[i][j]=1
ans=2501

for i in range(a-7):
    for j in range(b-7):
        summ=0
         
        for k in range(i,i+8):
            for l in range(j,j+8):
                summ+=comp[k][l]

        if summ<ans:
            ans=summ

        
        
print(ans)




