#!/usr/bin/env python

import sys
input= sys.stdin.readline

n,k=map(int,input().split())
arr=[0 for _ in range(1000001)]
left,right=sys.maxsize, 0

for _ in range(n):
    g,x=map(int,input().split())
    arr[x]=g
    right=max(x,right)
    left=min(x,left)

end=left
now, ans=0,0

for srt in range(left,right+1):
    while end<right+1 and end-srt<=k*2:
        if not arr[end]:
            end+=1
            continue
        now +=arr[end]
        end+=1
    ans = max(ans,now)
    now-=arr[srt]
    if end>=right:
        break
print(ans)
    
 
