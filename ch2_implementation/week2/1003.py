T = int(input())
N_list = [int(input()) for _ in range(T)]
res = [[0 for _ in range(2)] for _ in range(T)]

def fibonacci(i, n):
  if (n == 0):
    res[i][0] += 1
    return 0
  elif (n == 1):
    res[i][1] += 1
    return 1
  else:
    return fibonacci(i, n - 1) + fibonacci(i, n - 2)

for i in range(T):
  n = N_list[i]
  fibonacci(i, n)

for i in range(T):
  print(f"{res[i][0]} {res[i][1]}")