#!/usr/bin/env python

n,m=map(int,input().split())

nums=[i+1 for i in range(n)]
check=[False]*n

ans=[]

def dfs(cnt):
    if cnt==m:
        print(*ans)
        return          
        # if문 안에 return _ return 지점에서 프로그램 종료 

    for i in range(n):
        print("for i : -------------- : ", i)
        if check[i]:        #check 이 true면 지나감
            continue

        check[i]=True
        ans.append(nums[i])
         
        dfs(cnt+1)      #여기서 이제 dfs. 한 노드 잡고 아래로 내려가다가
                        #그 노드 다 돌면, 옆 노드로 이동하는거지 sibling으로

        print("recur end _ i,cnt : ",i,cnt)
        ans.pop()
        # print("after pop : ", ans)
        check[i]=False
dfs(0)





