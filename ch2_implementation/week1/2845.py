L, P = map(int, input().split(' '))
total = L * P
participants = list(map(int, input().split(' ')))
for i in range(5):
	participants[i] -= total
print(' '.join(map(str, participants)))