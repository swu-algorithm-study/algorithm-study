N, M = map(int, input().split())

max_min_value = 0  # 최댓값 저장 변수

for _ in range(N):
    row = list(map(int, input().split()))
    min_value = min(row)  # 각 행의 최솟값 찾기 (O(M))
    max_min_value = max(max_min_value, min_value)  # 최댓값 갱신 (O(1))

print(max_min_value)  # 결과 출력