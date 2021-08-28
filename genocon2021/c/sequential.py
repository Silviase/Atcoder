DEBUG = False
MATCH = 1
MISMATCH = -3


def similarity(x, y):
    if x == y:
        return MATCH
    else:
        return MISMATCH


def alignment(s, t, forbid_s_gap=False):
    if DEBUG:
        print("s:", s)
        print("t:", t)
    dp = [[-1e9 for i in range(len(t) + 1)] for j in range(len(s) + 1)]
    prev = [[(-1, -1) for i in range(len(t) + 1)] for j in range(len(s) + 1)]
    for i in range(1, len(s) + 1):
        dp[i][0] = MISMATCH * i
        prev[i][0] = (i - 1, 0)
    for j in range(1, len(t) + 1):
        dp[0][j] = MISMATCH * j
        prev[0][j] = (0, j - 1)

    dp[0][0] = 0

    for i in range(len(s)):
        for j in range(len(t)):
            dp[i + 1][j + 1] = dp[i][j] + similarity(s[i], t[j])
            prev[i + 1][j + 1] = (i, j)
            # t[j]だけ使われる <=> s にgap
            if not forbid_s_gap:
                if dp[i + 1][j] + similarity(t[j], "-") > dp[i + 1][j + 1]:
                    dp[i + 1][j + 1] = dp[i + 1][j] + similarity("-", t[j])
                    prev[i + 1][j + 1] = (i + 1, j)
            # s[i]だけ使われる <=> t にgap
            if dp[i][j + 1] + similarity(s[i], "-") > dp[i + 1][j + 1]:
                dp[i + 1][j + 1] = dp[i][j + 1] + similarity(s[i], "-")
                prev[i + 1][j + 1] = (i, j + 1)
    return dp, prev


def backtrack(s, t, prev):
    s_aln, t_aln = "", ""
    i, j = len(s), len(t)
    while i > 0 or j > 0:
        ni, nj = prev[i][j]
        s_aln += s[i - 1] if ni != i else "-"
        t_aln += t[j - 1] if nj != j else "-"
        i, j = ni, nj
    return s_aln[::-1], t_aln[::-1]


N = int(input())
max_len = -1
genoms = []
aligned_genoms = []
for _ in range(N):
    genoms.append(input())

dp, prev = alignment(genoms[0], genoms[1], False)
g1, g2 = backtrack(genoms[0], genoms[1], prev)
aligned_genoms.append(g1)
aligned_genoms.append(g2)
max_len = max(max_len, len(g1))

for i in range(2, N):
    dp, prev = alignment(g1, genoms[i], True)
    g1, g2 = backtrack(g1, genoms[i], prev)
    aligned_genoms.append(g2)
    max_len = max(max_len, len(g1))

for genom in aligned_genoms:
    print("-" * (max_len - len(genom)) + genom)
