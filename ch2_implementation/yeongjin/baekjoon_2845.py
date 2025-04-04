ppl, area = map(int, input().split())
news = list(map(int, input().split()))
correct = ppl*area

for n in news:
    print(n - correct, end=' ')
