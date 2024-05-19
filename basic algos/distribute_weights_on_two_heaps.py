from collections import Counter


def build_two_servers(gpus: tuple) -> tuple:
    W = sum(gpus) // 2
    N = len(gpus)
    a = [0] + sorted(list(gpus))

    if N == 0:
        return ((), (), ())

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

    # for plain in dp:
    #     for row in plain:
    #         print(*row)
    #     print()
    #
    # print('~' * 10)
    #
    # for plain in prev1:
    #     print(*plain)
    # print(max_value)

    i, j = max_value, max_value
    serv_1 = []
    serv_2 = []
    while prev1[i][j] != 0:
        while i > 0:
            serv_1.append(w)
            i -= w
            w = prev1[i][j]
            while j > 0:
                serv_2.append(w)
                j -= w
                w = prev1[i][j]


    unused = tuple((Counter(a) - Counter(serv_1) - Counter(serv_2) - Counter([0])).elements())

    return (tuple(serv_1), tuple(serv_2), unused)


if __name__ == '__main__':
    various_gpus = (
        (1, 1),  # GPUs: (1, 1), server_0: (1), server_1: (1), unused: ()
        (1, 1, 2, 1),  # GPUs: (1, 1, 2, 1), server_0: (1, 1), server_1: (2), unused: (1)
        (3, 1),  # GPUs: (3, 1), server_0: (), server_1: (), unused: (1, 3)
        (),  # GPUs: (), server_0: (), server_1: (), unused: ()
        (2, 2, 5, 6, 7, 3),  # ...
        (78, 35, 34, 1, 2, 3, 1, 2, 1, 1)
    )

    for gpus in various_gpus:
        result = build_two_servers(gpus)
        print(f"GPUs: {gpus}, server_0: {result[0]}, server_0: {result[1]}, unused: {result[2]}")
        assert sum(result[0]) == sum(result[1])