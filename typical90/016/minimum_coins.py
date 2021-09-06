N = int(input())
A, B, C = map(int, input().split())
# 合計10000枚ならA,Bで利用できる可能性は10000C2で10^8よりは小さくなりそうなので，そこで判断すればいい

mini = 10000
for i in range(10000):
    for j in range(10000 - i):
        to_pay_by_c = N - A * i - B * j
        if to_pay_by_c % C == 0 and to_pay_by_c >= 0:
            mini = min(mini, i + j + to_pay_by_c // C)

print(mini)