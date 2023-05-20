for i in range(1,11):
    dump=int(input())
    li=list(map(int,input().split()))
    while dump>0:
        li.sort()
        li[0]+=1
        li[-1]-=1
        dump-=1
    li.sort()
    ans=li[-1]-li[0]
    print(f'#{i} {ans}')
