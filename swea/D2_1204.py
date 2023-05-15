n=int(input())
for i in range(1,n+1):
    case_num=int(input())
    li=[0 for _ in range(101)]
    scores=list(map(int,input().split()))
    for score in scores:
        li[score]+=1
    maxx=-1
    #maxx=max(li)
    for i in range(0,101):
    	if li[i]>=maxx:
            maxx=li[i]
            ans=i
    #print(f'#{case_num} {li.index(maxx)}')
    print(f'#{case_num} {ans}')
