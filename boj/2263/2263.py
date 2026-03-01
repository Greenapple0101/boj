import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

n = int(input())

inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))
preorder = []
pos = [0] * (n + 1)
for i in range(n):
    pos[inorder[i]] = i


def dfs(in_start, in_end, post_start, post_end):
    root = postorder[post_end]
    r = pos[root]

    if in_start > in_end or post_start > post_end:
        return

    len_left_tree = r - in_start

    print(root, end=' ')
    dfs(in_start, r - 1, post_start, post_start + len_left_tree - 1)
    dfs(r + 1, in_end, post_start + len_left_tree, post_end - 1)


dfs(0, n - 1, 0, n - 1)