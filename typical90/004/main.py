def cross_sum(H, W, array):
    sum_row = [0] * H
    sum_col = [0] * W
    for i in range(H):
        for j in range(W):
            sum_row[i] += array[i][j]
            sum_col[j] += array[i][j]
    xsum = [[0 for _ in range(W)] for _ in range(H)]
    for i in range(H):
        for j in range(W):
            xsum[i][j] = sum_row[i] + sum_col[j] - array[i][j]
    return xsum


H, W = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(H)]

for ls in cross_sum(H, W, array):
    print(" ".join(map(str, ls)))