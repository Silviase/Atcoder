def simirality(x, y):
    if x == y and x != '-':
        return 1
    elif x == '-' or y == '-':
        return -5
    else:
        return -3



s = input()
t = input()
dp, bef = alignment(s, t)
s_aln, t_aln = backtrack(s, t, bef)
print(s_aln)
print(t_aln)