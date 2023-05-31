#!/usr/bin/env python

doc={'0':'zero','1':'one','2':'two','3':'three','4':'four','5':'five','6':'six','7':'seven','8':'eight','9':'nine'}

m,n=map(int,input().split())
li=[]
for i in range(m,n+1):
    s = ' '.join([doc[c] for c in str(i)])
    li.append([i, s])
li.sort(key=lambda x:x[1])
for i in range(len(li)):
    if i%10 == 0 and i!= 0:
        print()
    print(li[i][0], end=' ')
