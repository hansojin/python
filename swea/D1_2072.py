n=int(input())
for i in range(1,n+1):
    li=[]
    sum=0
    li=list(map(int,input().split()))
    for num in li:
        if num%2==1:
            sum+=num
    print(f'#{i} {sum}')
