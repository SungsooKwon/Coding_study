# 컴퓨터 상호 간 정보 교환
# A - B 연결 B - C 연결 A - C 간접적 연결
# n : 컴퓨터 개수 / 연결 정보 -> 1 : o 0: x -> return 네트워크 개수

from collections import deque

def solution(n, computers):
    visited = [False] * n
    answer = 0
    
    def bfs(start):
        queue = deque()
        queue.append(start)
        visited[start] = True
        
        while queue:
            node = queue.popleft()
            for next_node in range(n):
                if not visited[next_node] and computers[node][next_node] == 1:
                    visited[next_node] = True
                    queue.append(next_node)
                    
    for i in range(n):
        if not visited[i]:
            bfs(i)
            answer += 1
        
    return answer