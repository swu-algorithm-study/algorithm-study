l, p = map(int, input().split())
numList = list(map(int, input().split()))

for num in numList:
    print(num - l*p, end=' ')