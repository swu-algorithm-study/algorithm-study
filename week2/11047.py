N, K = map(int, input().split(' '))
coins = []
for i in range(N):
	coins.append(int(input()))
coins.reverse()

result = 0
for c in coins:
	if c > K:
		continue
	result += K // c
	K -= c * (K // c)

print(result)