from collections import deque
n, m = map(int, input().split(" "))

graph = []

for i in range(n):
    graph.append(list(map(int, input().split(" "))))

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] # 상 하 좌 우
distance = [[-1 if graph[i][j] == 1 else 0 for j in range(m)] for i in range(n)]

queue = deque()

for i in range(n):
    for j in range(m):
        if graph[i][j] == 2: # 목표 지점
            queue.append((i, j))
            distance[i][j] = 0 # 목표 지점(2) <- 0 넣기
            
while queue:
    x, y = queue.popleft()
    
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
    
        if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1 and distance[nx][ny] == -1:
            queue.append((nx, ny))
            distance[nx][ny] = distance[x][y] + 1
            
# 결과 출력
for row in distance:
    print(" ".join(map(str, row)))
