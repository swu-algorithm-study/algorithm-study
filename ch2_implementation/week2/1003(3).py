T = int(input())
N_list = [int(input()) for _ in range(T)]

f = [[1, 0], [0, 1]]

def fib(n):
    while len(f) <= n:
        zero = f[-1][0] + f[-2][0]
        one = f[-1][1] + f[-2][1]
        f.append([zero, one])

for n in N_list:
    fib(n)
    print(f"{f[n][0]} {f[n][1]}")