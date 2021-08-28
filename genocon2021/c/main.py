MATCH = 0
MISMATCH = -1
DEBUG = True


def similarity(x, y):
    if x == y:
        return MATCH
    else:
        return MISMATCH


def alignment(s, t, forbid_s_gap=False):
    dp = [[-1e9 for i in range(len(t) + 1)] for j in range(len(s) + 1)]
    bef = [[(i - 1, j - 1) for i in range(len(t) + 1)]
           for j in range(len(s) + 1)]
    dp[0][0] = 0
    for i in range(1, len(s) + 1):
        bef[i][0] = (i - 1, 0)
    for j in range(1, len(t) + 1):
        bef[0][j] = (0, j - 1)

    for i in range(len(s)):
        for j in range(len(t)):
            # default: match
            if s[i] == t[j]:
                dp[i + 1][j + 1] = dp[i][j] + similarity(s[i], t[j])
                bef[i + 1][j + 1] = (i, j)
            else:
                dp[i + 1][j + 1] = dp[i + 1][j] + MISMATCH
                bef[i + 1][j + 1] = (i + 1, j)
                # s側にgapが入る
                if not forbid_s_gap and dp[i][j + 1] + MISMATCH > dp[i + 1][j +
                                                                            1]:
                    dp[i + 1][j + 1] = dp[i][j + 1] + MISMATCH
                    bef[i + 1][j + 1] = (i, j + 1)
    return dp, bef


def backtrack(s, t, bef):
    if DEBUG:
        print("backtrack", s, t)
    s_aln, t_aln = "", ""
    i, j = len(s), len(t)
    while i > 0 or j > 0:
        ni, nj = bef[i][j]
        if DEBUG:
            print(f"({i}, {j}) -> ({ni}, {nj})")
        s_aln += s[i - 1] if ni < i else "-"
        t_aln += t[j - 1] if nj < j else "-"
        i, j = ni, nj
    return s_aln[::-1], t_aln[::-1]


N = int(input())
genoms = []
for _ in range(N):
    genoms.append(input())
result = []
for i in range(1, N):
    if i == 1:
        _, track = alignment(genoms[0], genoms[i], forbid_s_gap=False)
        g1, g2 = backtrack(genoms[0], genoms[i], track)
        if DEBUG:
            print("g1:", g1)
            print("g2:", g2)
        source = g1
        result.append(g1)
        result.append(g2)
    else:
        if DEBUG:
            print("res", source)
        _, track = alignment(source, genoms[i], forbid_s_gap=True)
        h1, h2 = backtrack(source, genoms[i], track)
        if DEBUG:
            print("h1:", h1)
            print("h2:", h2)
        h2 += "-" * (len(h1) - len(h2))
        result.append(h2)

assert len(result) == N
for r in result:
    print(r)
