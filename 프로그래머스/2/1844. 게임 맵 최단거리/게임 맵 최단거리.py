from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    
    # 북, 남, 서, 동 방향
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    visited = [[False] * m for _ in range(n)]
    queue = deque()
    queue.append((0, 0))
    visited[0][0] = True
    
    # 시작 위치의 값을 1로 두고, 거리 누적
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            # 범위 안에 있고, 벽이 아니며, 아직 방문 안한 곳이면
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = True
                maps[nx][ny] = maps[x][y] + 1  # 이전 거리 + 1
                queue.append((nx, ny))
    
    # 도착 지점이 여전히 1이면 도달 불가
    return maps[n-1][m-1] if maps[n-1][m-1] != 1 else -1