N,K= map(int, input().split())

count =0 

while(1):
  if N/ K ==1:
    count+=1
    break
  if N% K ==0:
    count+=1
    N= N/K
  elif N/ K !=0:
    count+=1
    N= N-1

print(count)

#O(logkN)으로 매우 효율적