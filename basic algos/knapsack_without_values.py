W, n = map(int, input().split())
a = list(map(int, input().split())) + [0]

dp = [[0] * (W+1) for _ in range(n+1)]

for i in range(n+1):
    dp[i][0] = 1

max_j = 0
for i in range(0, n+1):
    for j in range(1, W + 1):
        dp[i][j] = dp[i-1][j]
        if a[i] <= j and dp[i - 1][j - a[i]]:
            dp[i][j] = 1
            max_j = max(j, max_j)

print(max_j)