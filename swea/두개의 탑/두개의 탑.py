T=int(input())
for tc in range(T):
    N,M1,M2=map(int,input().split())
    lst=list(map(int,input().split()))
    lst.sort(reverse=True)
    m=min(M1,M2)
    sum=0
    cnt=0
    for i in range(m):
        sum+=(lst[2*i]+lst[2*i+1])*(i+1)
        cnt=i+1

    for j in range(2*m,N):
        sum+=lst[j]*(cnt+1)
        cnt+=1

    print(f"#{tc+1} {sum}")