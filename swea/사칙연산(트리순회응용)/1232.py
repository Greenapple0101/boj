for tc in range(1, 11):
    N = int(input())
    cal = [''] * (N + 1)
    adj = [[] for _ in range(N + 1)]
    for i in range(1, N + 1):
        lst = list(input().split())
        if (len(lst) == 2):
            cal[i] = (lst[1])
        if (len(lst) == 4):
            cal[i] = (lst[1])
            adj[i].append(int(lst[2]))
            adj[i].append(int(lst[3]))


    def dfs(n):
        if (len(adj[n]) == 0):
            return int(cal[n])
        left = dfs(adj[n][0])
        right = dfs(adj[n][1])
        if (cal[n] == '*'):
            return left * right
        if (cal[n] == '/'):
            return left / right
        if (cal[n] == '-'):
            return left - right
        if (cal[n] == '+'):
            return left + right


    print(int(dfs(1)))