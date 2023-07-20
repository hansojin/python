#!/usr/bin/env python

def kmp(text,pattern):
    n=len(text)
    m=len(pattern)

    table=[0]*m
    
    j=0
    for i in range(1,m):
        while j>0 and pattern[i]!=pattern[j]:
            j=table[j-1]
        if pattern[i]==pattern[j]:
            j+=1
            table[i]=j
    
    j,cnt=0,0
    arr=[]
    for i in range(n):
        while j>0 and text[i]!=pattern[j]:
            j=table[j-1]
        if text[i]==pattern[j]:
            if j==(m-1):
                cnt+=1
                arr.append(i-m+2)
                j=table[j]
            else:
                j+=1
    print(cnt)
    print(*arr)

t=input()
p=input()
kmp(t,p)
