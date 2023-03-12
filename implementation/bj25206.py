#!/usr/bin/env python

cnt=0
sum=0

L = {'A+':4.5,'A0':4.0,'B+':3.5,'B0':3.0,'C+':2.5,'C0':2.0,'D+':1.5,'D0':1.0,'F':0.0}


'''
def cal(n,m):
    global cnt
    global sum

    if m=="A+":
        sum+=n*4.5
        cnt+=n
    elif m=="A0":
        sum+=n*4
        cnt+=n
    elif m=="B+":
        sum+=n*3.5
        cnt+=n
    elif m=="B0":
        sum+=n*3
        cnt+=n
    elif m=="C+":
        sum+=n*2.5
        cnt+=n
    elif m=="C0":
        sum+=n*2.0
        cnt+=n
    elif m=="D+":
        sum+=n*1.5
        cnt+=n
    elif m=="D0":
        sum+=n*1
        cnt+=n
    elif m=="F":
        cnt+=n
'''

for i in range(20):
    score=input().split()
    #cal(float(score[1]),score[2])
    
    if score[2]=="P":
        continue
    else:
        sum+=float(score[1])*L[score[2]]
        cnt+=float(score[1])

print(sum/cnt)

