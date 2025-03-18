def solution(L, P, V):
	result = (V // P) * L + V % P
	return result

res = list()
while True:
	L, P, V = map(int, input().split())
	if L == 0 and P == 0 and V == 0:
		break
	res.append(solution(L, P, V))

for i in range(len(res)):
	print(f"Case {i+1}: {res[i]}")