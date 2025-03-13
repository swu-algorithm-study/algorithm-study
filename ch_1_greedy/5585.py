m=int(input())

money=[500,100,50,10,5,1]
change=1000-m 
count=0
for i in money:
    count +=change//i 
    change %= i 

print(count)