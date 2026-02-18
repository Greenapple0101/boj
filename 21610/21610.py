N,M=map(int,input().split())
grid=[list(map(int,input().split())) for _ in range(N)]
moves=[list(map(int,input().split())) for _ in range(M)]

dx=[-1,-1,0,1,1,1,0,-1]
dy=[0,1,1,1,0,-1,-1,-1]
cloud=[(N-1,0),(N-1,1),(N-2,0),(N-2,1)]

for d,c in moves:
    moved_cloud=[]
    for r,c in cloud:
        nr=(r+dy[d]*c)%N
        nc=(c+dx[d]*c)%N
        moved_cloud.append((nr,nc))
    visited = [[False] * N for _ in range(N)]
    for r,c in moved_cloud:
        grid[r][c]+=1
        visited[r][c]=True
    for r,c in moved_cloud:
        for i in range(0,9,2):
            ni=(r+dy[i])%N
            nj=(c+dx[i])%N
            if(grid[ni][nj] is not 0):
                grid[r][c]+=1
    new_clouds=[]
    for i in range(N):
        for j in range(N):
            if(grid>=2 and not visited[i][j]):
                grid[r][c]-=2
                new_clouds.append((i,j))
    cloud=new_clouds
print(sum(sum(row) for row in grid))