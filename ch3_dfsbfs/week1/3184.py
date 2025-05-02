R, C = map(int, input().split(' '))
graph = [list(input()) for _ in range(R)]
visited = [[False]*C for _ in range(R)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
	stack = [(x, y)] # 탐색을 시작할 좌표
	# stack에는 앞으로 방문할 후보 위치들이 쌓임
	sheep = 0
	wolf = 0
	
	while stack: # stack이 빌 때까지 반복
		x, y = stack.pop() # 스택에서 하나 꺼냄
		if visited[x][y]: # 이미 방문한 곳이면 건너뛰기
			continue
		visited[x][y] = True # 방문한 곳이 아니라면 방문 처리
	
		# 양이 있으면
		if graph[x][y] == 'o':
			sheep += 1
		# 늑대가 있으면
		elif graph[x][y] == 'v':
			wolf += 1
		
		# 상하좌우 인접 좌표 탐색
		for i in range(4):
			nx = x + dx[i]
			ny = y + dy[i]
			if 0 <= nx < R and 0 <= ny < C:
				if not visited[nx][ny] and graph[nx][ny] != '#':
					stack.append((nx, ny)) # stack에 넣어서 다음 탐색 대상으로 등록
	return sheep, wolf

total_sheep = 0
total_wolf = 0

for i in range(R):
	for j in range(C):
		if not visited[i][j] and graph[i][j] != '#':
			sheep, wolf = dfs(i, j)
			if sheep > wolf:
				total_sheep += sheep
			else:
				total_wolf += wolf

print(total_sheep, total_wolf)