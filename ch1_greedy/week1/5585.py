money = int(input())
money = 1000 - money

changes = [500, 100, 50, 10, 5, 1]

result = 0
for i in changes:
	if i > money:
		continue
	tmp = money // i
	result += tmp
	money -= i * tmp
	continue

print(result)