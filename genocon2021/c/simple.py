# Small: [115, 116]
# Large: [0, 0, 0, 0, 0, 0, 0, 0]
# smallでは正の点数が取れたが，Largeでは正の点数すら取れませんでした．

N = int(input())
genoms = []
max_len = 0
for i in range(N):
    genoms.append(input())
    if len(genoms[i]) > max_len:
        max_len = len(genoms[i])

for i in range(N):
    print(genoms[i] + '-' * (max_len - len(genoms[i])))
