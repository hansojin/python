num=int(input())
for i in range(1,num+1):
    n=int(input())
    li=list(map(int,input().split()))
    maxx,ans=0,0
    for nums in li[::-1]:
        if nums>maxx:
            maxx=nums
        else:
            ans+=maxx-nums

    print(f'#{i} {ans}')

