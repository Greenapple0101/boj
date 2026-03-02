T=int(input())

def dfs(n):
    global cnt
    if(n>N):
        return
    dfs(2*n)
    tree[n]=cnt
    cnt+=1
    dfs(2*n+1)

for tc in range(1,T+1):
    N=int(input())
    tree=[0]*(N+1)
    cnt=1

    dfs(1)

    print(f"#{tc} {tree[1]} {tree[N//2]}")