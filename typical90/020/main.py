# log_2 a < b log_2 c <=> a < 2^b * c
a, b, c = map(int, input().split())
if a < c**b:
    print('Yes')
else:
    print('No')