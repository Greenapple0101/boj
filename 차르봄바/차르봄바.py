T=int(input())
for tc in range(T):
    N,P=map(int,input().split())
    grid=[list(map(int,input().split())) for _ in range(N)]
    dy=[0,0,1,-1]
    dx=[1,-1,0,0]
    maxy=0
    for i in range(N):
        for j in range(N):
            sum = grid[i][j]
            cnt = 1
            while(cnt!=P+1):
                for k in range(4):
                    ni = i + dy[k]*cnt
                    nj = j + dx[k]*cnt
                    if (0 <= ni < N and 0 <= nj < N):
                        sum+=grid[ni][nj]
                cnt+=1
            maxy=max(maxy,sum)

    print(f"#{tc+1} {maxy}")