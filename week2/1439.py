input_str = input()
l = len(input_str)

i = 0
tmp = 0
chunks = []
while i < l-1:
	if input_str[i] != input_str[i+1]:
		chunks.append(input_str[tmp:i+1])
		tmp = i + 1
	i += 1
chunks.append(input_str[tmp:])

num_0 = 0
num_1 = 0
for ch in chunks:
	if '0' in ch:
		num_0 += 1
	elif '1' in ch:
		num_1 += 1

print(min(num_0, num_1))