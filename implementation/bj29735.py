#!/usr/bin/env python

a,b=input().split()
ah,am=map(int,a.split(":"))
bh,bm=map(int,b.split(":"))
diff = (bh*60+bm) - (ah*60+am)

n,t = map(int,input().split())
psb = diff//t
if diff%t==0:
    psb-=1
print(n//psb)
tim = t*(n%psb+1)
h,m=ah,am
m+=tim

while True:
    if m<60:
        break
    else:
        m-=60
        h+=1
print('%02d:%02d' %(h,m))

