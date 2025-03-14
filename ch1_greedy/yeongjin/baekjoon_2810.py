n = int(input())
seats = input()

count_LL = 0
i=0

while i < n-1 :
    if seats[i] == 'L' and seats[i+1] == 'L' :
        count_LL +=1
        i+=2
    else:
        i+=1

print(min(n,n +1 -count_LL))