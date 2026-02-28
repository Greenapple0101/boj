T=int(input())

for tc in range(T):
    N=int(input())
    grid=[list(map(int,input().split())) for _ in range(N)]
    arr=[[] for _ in range(21)]
    for num in range(1,21):
        for i in range(N):
            for j in range(N):
                if(grid[i][j]==num):
                    arr[num].append((i,j))
    maxy=0
    for k in range(21):
        for r,c in arr[k]:
            for r1,c1 in arr[k]:
                if (r1 < r or c1 < c): continue
                maxy=max(maxy,(r1-r+1)*(c1-c+1))
    ans=0
    visited=[]
    for k in range(21):
        for r,c in arr[k]:
            for r1,c1 in arr[k]:
                if(maxy==(r1-r+1)*(c1-c+1)):
                    if(r1<r or c1<c): continue
                    ans+=1
    print(f"#{tc+1} {ans}")