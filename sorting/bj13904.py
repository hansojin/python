#!/usr/bin/env python

import sys
input = sys.stdin.readline

arr=[]
ans=[0 for _ in range(1001)]
n=int(input())
for i in range(n):
    a,b=map(int,input().split())
    arr.append([a,b])

arr.sort(key=lambda x : -x[1])
# 일단 점수대로 내림차순

for i in range(n):
    for j in range(arr[i][0]-1,-1,-1):
        if ans[j]==0:
            ans[j]=arr[i][1]
            break
        #주어진 마감일로 부터, 첫날까지 스케줄이 비어있으면 점수 저장,
        #안비어있으면, ans[0]까지 살펴보면서 비었을때 저장
print(sum(ans))
