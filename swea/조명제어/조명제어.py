T=int(input())


for tc in range(T):
    N=int(input())
    lst=list(map(int,input().split()))
    lsst=[0 for _ in range(N)]
    countt=0
    while(lst!=lsst):
        for i in range(N):
            if(lst[i]!=lsst[i]):
                for k in range(i,N,i+1):
                    if(lsst[k]==0):
                        lsst[k]=1
                    elif(lsst[k]==1):
                        lsst[k]=0
                countt+=1
    print(f"#{tc+1} {countt}")
