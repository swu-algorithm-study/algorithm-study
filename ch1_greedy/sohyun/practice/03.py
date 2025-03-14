N,M= map(int,input().split())

array=[list(map(int, input().split())) for _ in range(N)]

array2=[]

for i in range(N):
  array[i]= sorted(array[i])

for i in range(N):
  array2.append(array[i][0])

print(max(array2))

