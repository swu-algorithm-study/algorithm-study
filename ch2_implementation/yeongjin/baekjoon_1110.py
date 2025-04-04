n=int(input())
x,y,cnt=0,0,1
new=(n%10)*10+(n%10+n//10)%10
while True:
    if new!=n:
        x,y=new//10,new%10
        new=y*10+(x+y)%10
        cnt+=1
    else:
        break
print(cnt)
