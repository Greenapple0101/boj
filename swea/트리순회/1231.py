for test_case in range(1, 11):
    N = int(input())
    adj=[[] for _ in range(N+1)]
    word=[' ']*(N+1)
    for i in range(1,N+1):
        lst=list(input().split())
        if(len(lst)==4):
            word[i]=lst[1]
            adj[i].append(int(lst[2]))
            adj[i].append(int(lst[3]))
        elif (len(lst) == 3):
            word[i] = lst[1]
            adj[i].append(int(lst[2]))
        elif (len(lst) == 2):
            word[i]=lst[1]
    print(adj)
    def dfs(n):

        if(len(adj[n])>=1):dfs(adj[n][0])
        print(word[n], end=' ')
        if(len(adj[n])>=2):dfs(adj[n][1])

    dfs(1)
    print("\n")