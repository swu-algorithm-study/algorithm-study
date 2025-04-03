N, M = map(int, input().split())
bulbs = list(map(int, input().split()))	# 전구 상태 리스트

for _ in range(M) :
    a, b, c = map(int, input().split())
    if a == 1 :	# 1번 명령어
        bulbs[b-1] = c
    elif a == 2 :	# 2번 명령어
        for i in range(b-1, c) :
            if bulbs[i] == 1 :
                bulbs[i] = 0 
            elif bulbs[i] == 0 :
                bulbs[i] = 1
    elif a == 3 :	# 3번 명령어
        for i in range(b-1, c) :
            bulbs[i] = 0
    elif a == 4 :	# 4번 명령어
        for i in range(b-1, c) :
            bulbs[i] = 1

print(*bulbs)