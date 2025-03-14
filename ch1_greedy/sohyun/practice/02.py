N,M,K= map(int, input().split())

array= list(map(int,input().split()))


total= 0

array= sorted(array)

max_num= array[-1]

for i in range(M):
  if i%(K+1) ==K:
    total +=array[-2]
  else:
    total+=max_num
    
print(total)
