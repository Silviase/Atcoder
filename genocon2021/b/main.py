def similarity(x, y):
    if x == y and x != '-':
        return 1
    elif x == '-' or y == '-':
        return -5
    else:
        return -3


def alignment(s, t):
    dp = [[-1e9 for i in range(len(t) + 1)] for j in range(len(s) + 1)]
    bef = [[(-1, -1) for i in range(len(t) + 1)] for j in range(len(s) + 1)]
    for i in range(len(s) + 1):
        dp[i][0] = -5 * i
        bef[i][0] = (i - 1, 0)
    for j in range(len(t) + 1):
        dp[0][j] = -5 * j
        bef[0][j] = (0, j - 1)
    bef[0][0] = (-1, -1)

    for i in range(len(s)):
        for j in range(len(t)):
            dp[i + 1][j +
                      1], bef[i +
                              1][j +
                                 1] = dp[i][j] + similarity(s[i], t[j]), (i, j)
            if dp[i + 1][j] + similarity(s[i], "-") > dp[i + 1][j + 1]:
                dp[i + 1][j + 1], bef[i + 1][j +
                                             1] = dp[i + 1][j] + similarity(
                                                 s[i], "-"), (i + 1, j)
            if dp[i][j + 1] + similarity("-", t[j]) > dp[i + 1][j + 1]:
                dp[i + 1][j + 1], bef[i + 1][j +
                                             1] = dp[i][j + 1] + similarity(
                                                 "-", t[j]), (i, j + 1)
    return dp, bef


def backtrack(s, t, bef):
    s_aln, t_aln = "", ""
    i, j = len(s), len(t)
    while i > 0 or j > 0:
        ni, nj = bef[i][j]
        s_aln += s[i - 1] if ni != i else "-"
        t_aln += t[j - 1] if nj != j else "-"
        i, j = ni, nj
    return s_aln[::-1], t_aln[::-1]


s = input()
t = input()
dp, bef = alignment(s, t)
s_aln, t_aln = backtrack(s, t, bef)
print(s_aln)
print(t_aln)