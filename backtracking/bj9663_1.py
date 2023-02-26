n=int(input())
visit=[True]*n

down_visit=[True]*(2*n-1)    #\ 대각선
up_visit=[True]*(2*n-1)      #/ 대각선

cnt=0
col=[]

def n_queen(k):
    global cnt
    if k==n:
        cnt+=1
    else:
        for i in range(n):
            if visit[i] and down_visit[i-k] and up_visit[i+k]:
               
                visit[i]=False
                down_visit[i-k]=False
                up_visit[i+k]=False
                
                n_queen(k+1)
                
                visit[i]=True
                down_visit[i-k]=True
                up_visit[i+k]=True
n_queen(0)
print(cnt)
