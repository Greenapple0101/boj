T=int(input())

def dfs(n):
    if n>N:
        return 0

    if(tree[n]):
        return tree[n]

    tree[n]=dfs(2*n)+dfs(2*n+1)
    return tree[n]

for tc in range(1,T+1):

    N,M,L=map(int,input().split())
    tree=[0]*(N+1)
    for _ in range(M):
        l,lv=map(int, input().split())
        tree[l]=lv
    print(dfs(L))
