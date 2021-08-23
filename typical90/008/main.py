# dp[i][j] = {文字列のi文字目の前まで利用したところで"atcoder"の[j]文字目まで完成している場合の数}
atcoder = "atcoder"


def atcounter(s):
    dp = [[0 for i in range(len(atcoder) + 1)] for j in range(len(s) + 1)]
    dp[0][0] = 1
    for i in range(1, len(s) + 1):
        dp[i][0] = 1

    for i in range(1, len(s) + 1):
        for j in range(1, len(atcoder) + 1):
            if s[i - 1] == atcoder[j - 1]:
                dp[i][j] = (dp[i - 1][j - 1] + dp[i - 1][j]) % 1000000007
            else:
                dp[i][j] = dp[i - 1][j]

    return dp[len(s)][len(atcoder)]


N = int(input())
S = input()
print(atcounter(S))
