for i in range(int(input())):
    li=list(map(int,input().split()))
    summ=sum(li)
    ans=summ/10
    print(f'#{i+1} {round(ans)}')
