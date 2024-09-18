def get_subsequence_count(s1, s2):
    n = len(s1)
    m = len(s2)
    # Initialize dp table with zeros
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    # Set base case: for the empty string s1, there's always one way to form it (by selecting nothing)
    for i in range(m + 1):
        dp[0][i] = 1

    # Fill the dp table using the same logic as the C++ version
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i][j - 1] + dp[i - 1][j - 1]
            else:
                dp[i][j] = dp[i][j - 1]

    return dp[n][m]

if __name__ == "__main__":
    s2 = "abcbabc"
    s1 = "abc"
    print(get_subsequence_count(s1, s2))
