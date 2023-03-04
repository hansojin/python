#!/usr/bin/env python

n=int(input())
df=[0]*(n+1)

for i in range(2,n+1):
    df[i]=df[i-1]+1
    if i%2==0:
        df[i]=min(df[i],df[i//2]+1)
    if i%3==0:
        df[i]=min(df[i],df[i//3]+1)
    #print(df[i])
print(df[n])

'''
bottom-up 풀이
1을 더하거나, /3하거나 /2 를 수행했을때 +=1 해주고, 
이 값들 중에 min을 뽑아서 다음 for문에서 사용하면서 진행
'''
