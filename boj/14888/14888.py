from collections import deque
import math
n = int(input())
numbers = list(map(int, input().split()))
operations = list(map(int, input().split()))
cal=['+']*operations[0]+['-']*operations[1]+['*']*operations[2]+['/']*operations[3]
visited=[0]*n

maxx=-1e9
minn=1e9
count=0
def dfs(level,res):
  global maxx,minn,count
  if(level==n-1):
    maxx=max(maxx,res)
    minn=min(minn,res)
    return
  for i in range(n-1):
    if(visited[i]):continue
    visited[i]=1
    if(cal[i]=='+'):dfs(level+1,res+numbers[level+1])
    if(cal[i]=='-'):dfs(level+1,res-numbers[level+1])
    if(cal[i]=='/'):
      dfs(level+1,int(res/numbers[level+1]))
    if(cal[i]=='*'):dfs(level+1,res*numbers[level+1])
    visited[i]=0

dfs(0,numbers[0])
print(maxx)
print(minn)