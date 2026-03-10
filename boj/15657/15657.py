n,m = map(int, input().split())
lst=list(map(int,input().split()))
lst.sort()
#저건 중복조합이다
def dfs(level,start,curr_lst):
  if(level==m):
    print(*curr_lst)
    return

  for i in range(start,n):
    dfs(level+1,i,curr_lst+[lst[i]])

dfs(0,0,[])
