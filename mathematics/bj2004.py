#!/usr/bin/env python


m,n=map(int,input().split())

def cnt_num(n,k):
    cnt=0
    while n:
        n//=k
        cnt+=n
    return cnt

five = cnt_num(m,5)-cnt_num(n,5)-cnt_num(m-n,5)
two = cnt_num(m,2)-cnt_num(n,2)-cnt_num(m-n,2)

print(min(five,two))
