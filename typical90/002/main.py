import itertools

def make_parenteses(seq):
    s = [")" for _ in range(len(seq)*2)]
    for i in seq:
        s[i] = "("
    return s

def valid_parenteses(s):
    stack = []
    for i in s:
        if i == "(":
            stack.append(i)
        else:
            if len(stack) == 0:
                return False
            stack.pop()
    return len(stack) == 0

def encyclopedia_of_parenteses(N):
    if N % 2 != 0:
        return
    candidate = list(itertools.combinations(range(N), N//2))
    for seq in candidate:
        s = make_parenteses(seq)
        if valid_parenteses(s):
            print("".join(s))
    return


N = int(input())
encyclopedia_of_parenteses(N)