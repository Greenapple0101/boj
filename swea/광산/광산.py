T=int(input())
dy=[0,0,-1,1]
dx=[1,-1,0,0]
def bfs(i,j): #동굴의 사이즈와 채굴량을 구하는 함수입니다
    q=[(i,j)]
    size=1
    sum=grid[i][j]
    visited[i][j] = 1
    while(q):
        y = q[0][0]
        x = q[0][1]

        q.pop(0)
        for i in range(4):
            ny=y+dy[i]
            nx=x+dx[i]
            if(ny<0 or ny>=N or nx<0 or nx>=N or visited[ny][nx]):continue
            if(grid[ny][nx]>0):
                size+=1
                visited[ny][nx] = 1
                q.append((ny, nx))
                sum+=grid[ny][nx]
    return sum, size



for tc in range(1,T+1):
    N=int(input())
    grid=[list(map(int,input().split())) for _ in range(N)]
    visited=[[0]*N for _ in range(N)]
    island_number=1
    island_p=[]

    for i in range(N):
        for j in range(N):
            if(grid[i][j]>0):island_p.append((i,j))
    ans=[]
    for i,j in island_p:
        if(visited[i][j]!=1): #한번 방문한 동굴은 방문하지 않기로 했습니다
            ans.append(bfs(i,j))
    ans.sort(key=lambda x:(-x[0],x[1]))
    print(ans[0])


