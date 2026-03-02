T=int(input())

def dfs(N):
    global count
    for val in tree[N]:
        dfs(val)
        count+=1
    return count

for tc in range(T):
    E,N=map(int,input().split())
    tree=[[] for _ in range(E+2)]
    lst=list(map(int,input().split()))

    for i in range(len(lst)//2):
        tree[lst[2*i]].append(lst[2*i+1])
    count=1
    print(dfs(N,0))