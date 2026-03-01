T=int(input())
for tc in range(T):
    N,M=map(int,input().split())
    ans=list(map(int,input().split()))
    student=[list(map(int,input().split())) for _ in range(N)]
    anss=[0]*(N)

    k=0
    for row in student:
        score = 0
        all = 0
        for i in range(M):
            if(row[i]==ans[i]):
                score+=1
                all+=score
            else:
                score=0
        anss[k]=all
        k+=1
    print(f"#{tc+1} {max(anss)-min(anss)}")