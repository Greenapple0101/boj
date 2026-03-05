import sys
input = sys.stdin.readline

R, C = map(int, input().split())

grid = [list(ord(c) - 65 for c in input().strip()) for _ in range(R)]

dy=[0,0,1,-1]
dx=[1,-1,0,0]
visited=[0]*26
visited[(grid[0][0])]=1
countt=1
max_ans=-1e9
def dfs(y,x):
  global countt,max_ans
  max_ans=max(max_ans,countt)
  for i in range(4):
    ny=y+dy[i]
    nx=x+dx[i]
    if(0<=ny<R and 0<=nx<C and visited[(grid[ny][nx])]==0):
      visited[(grid[ny][nx])]=1
      countt+=1
      dfs(ny,nx)
      countt-=1
      visited[(grid[ny][nx])]=0


dfs(0,0)
print(max_ans)