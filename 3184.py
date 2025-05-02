from collections import deque


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


R, C = map(int, input().split())
field = [list(input().strip()) for _ in range(R)]
visited = [[False] * C for _ in range(R)]

total_sheep = 0
total_wolf = 0

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True

    sheep = 0
    wolf = 0

    if field[x][y] == 'o':
        sheep += 1
    elif field[x][y] == 'v':
        wolf += 1

    while queue:
        cx, cy = queue.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0 <= nx < R and 0 <= ny < C:
                if not visited[nx][ny] and field[nx][ny] != '#':
                    visited[nx][ny] = True
                    queue.append((nx, ny))
                    if field[nx][ny] == 'o':
                        sheep += 1
                    elif field[nx][ny] == 'v':
                        wolf += 1
    return sheep, wolf

for i in range(R):
    for j in range(C):
        if not visited[i][j] and field[i][j] != '#':
            sheep, wolf = bfs(i, j)
            if sheep > wolf:
                total_sheep += sheep
            else:
                total_wolf += wolf

print(f"{total_sheep} {total_wolf}")
