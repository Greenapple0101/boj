n,m=map(int,input().split())
lst=list(map(int,input().split()))
lst.sort()
visited=[0]*(len(lst)+1)
def dfs(level,start,path):
  if(level==m):
    print(*path)
    return
  last_val=-1
  for i in range(start,len(lst)):
    if(last_val==lst[i]):continue
    last_val=lst[i]
    dfs(level+1,i,path+[lst[i]])


dfs(0,0,[])