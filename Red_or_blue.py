def mini_cost(red, blue, blue_cost):
    # 0 -- red, 1 -- blue
    n = len(red)

    dp = [[0] * 2 for _ in range(n + 1)]
    dp[0][0] = 0
    dp[0][1] = blue_cost
    ans = [0] * (n + 1)

    for i in range(1, n + 1):
        dp[i][0] = min(dp[i - 1][0] + red[i - 1], dp[i - 1][1] + red[i - 1])
        dp[i][1] = min(dp[i - 1][1] + blue[i - 1], dp[i - 1][0] + blue[i - 1] + blue_cost)
        ans[i] = min(dp[i][0], dp[i][1])

    return ans
