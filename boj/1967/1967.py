import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)
N=int(input())
adj=[[] for _ in range (N+1)]
parent=[]*(N+1)
for _ in range(1,N):
  p,c,g=list(map(int,input().split()))
  adj[p].append((c,g))
  adj[c].append((p,g))

max_gram=0
gram=0
lst=[]
idx=0
visited=[0]*(N+1)
def dfs(n,gram):
  global max_gram,idx
  visited[n]=1
  if(len(adj[n])==1):
    if(gram>max_gram):
      max_gram=gram
      idx=n

  for val in adj[n]:
    if(visited[val[0]]):continue
    dfs(val[0],gram+val[1])

dfs(1,0)
visited=[0]*(N+1)
dfs(idx,0)
print(max_gram)