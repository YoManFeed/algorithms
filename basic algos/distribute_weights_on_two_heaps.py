# W, n = map(int, input().split())
# a = [0] + list(map(int, input().split()))

# W, N = 10, 4
# a = [0, 1, 2, 3, 4]

W, N = 10, 3
a = [0, 2, 3, 5]

W, N = 14, 4
a = [0, 1, 1, 3, 4]

W = W // 2

dp = [[[0] * (W + 1) for _ in range(W + 1)] for _ in range(N + 1)]
for i in range(N+1):
    dp[i][0][0] = 1


prev1 = [['.'] * (W+1) for _ in range(W+1)]

max_value = 0
for n in range(N+1):
    for i in range(0, W+1):
        for j in range(0, W+1):
            dp[n][i][j] = dp[n-1][i][j]
            w = a[n]
            if w <= j and dp[n-1][i][j-w]:
                dp[n][i][j] = 1
                if prev1[i][j] == '.':
                    prev1[i][j] = w
            if w <= i and dp[n-1][i-w][j]:
                dp[n][i][j] = 1
                if prev1[i][j] == '.':
                    prev1[i][j] = w
            if i == j and dp[n][i][j]:
                max_value = max(max_value, i)

for plain in dp:
    for row in plain:
        print(*row)
    print()

print('~'*10)

for plain in prev1:
    print(*plain)
print(max_value)

i, j = max_value, max_value
ans1 = []
ans2 = []
while prev1[i][j] > 0:
    while i > 0:
        ans1.append(w)
        i -= w
        w = prev1[i][j]

    while j > 0:
        ans2.append(w)
        j -= w
        w = prev1[i][j]

print(ans1, ans2)