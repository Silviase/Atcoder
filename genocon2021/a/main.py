def compl_chain(seq):
    compl_dict = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
    return ''.join([compl_dict[base] for base in seq[::-1]])


N = int(input())
for _ in range(N):
    s = input()
    print(compl_chain(s))
