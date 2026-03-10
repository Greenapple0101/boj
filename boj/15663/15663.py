n, m = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
visited2 = [0] * (len(lst) + 1)


def dfs(level, start, curr_lst):
    if (level == m):
        print(*curr_lst)
        return
    last_val = -1
    for i in range(len(lst)):
        if (last_val == lst[i]): continue
        if (visited2[i]): continue
        visited2[i] = 1
        last_val = lst[i]
        dfs(level + 1, i, curr_lst + [lst[i]])
        visited2[i] = 0


dfs(0, 0, [])