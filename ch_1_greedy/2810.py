a=int(input())
n=input()

couple= n.count('LL')

if couple <=1:
    print(a)
else:
    print(a+1-couple)