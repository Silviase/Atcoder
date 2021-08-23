import itertools

S, K = input().split()
K = int(K)

print("".join(
    sorted(list(set(list(itertools.permutations(S, len(S))))))[K - 1]))
