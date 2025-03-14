N = int(input())
res = 1000 - N  # 거스름돈 계산
count = 0

coins = [500, 100, 50, 10, 5, 1]  # 사용할 동전 리스트

for coin in coins:
    count += res // coin  # 해당 동전 개수 추가
    res %= coin  # 남은 금액 업데이트

print(count)