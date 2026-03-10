n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
#동전 n개 사용했을 때 최댓값을 써야하나

dp=[0]*(k+1)
dp[0]=1
for c in coins:
  for i in range(c, k + 1):
    dp[i]=dp[i-c]+dp[i]

print(dp[k])