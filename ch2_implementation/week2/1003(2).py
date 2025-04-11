# 0 -> 1 0
# 1 -> 0 1
# 2 -> 1 1
# 3 -> 1 2
# 4 -> 2 3
# ...

T = int(input())
N_list = [int(input()) for _ in range(T)]

max_n = max(N_list)
f = [[0, 0] for _ in range(max_n+1)]
f[0] = [1, 0]
if max_n >= 1:
  f[1] = [0, 1]

for i in range(2, max_n+1):
  f[i][0] = f[i-1][0] + f[i-2][0]
  f[i][1] = f[i-1][1] + f[i-2][1]

for n in N_list:
  print(f"{f[n][0]} {f[n][1]}")