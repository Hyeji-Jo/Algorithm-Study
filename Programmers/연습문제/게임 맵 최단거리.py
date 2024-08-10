# 다른 사람의 풀이
from collections import deque

def solution(maps):
    # 맵의 크기
    n = len(maps)
    m = len(maps[0])
    
    # BFS를 위한 큐 초기화
    queue = deque([(0, 0, 1)])  # (x, y, distance)
    
    # 방문 여부를 확인할 배열
    visited = [[False] * m for _ in range(n)]
    visited[0][0] = True
    
    # 4방향 이동
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    while queue:
        x, y, distance = queue.popleft()
        
        # 목표 지점에 도착한 경우
        if x == n - 1 and y == m - 1:
            return distance
        
        # 4방향으로 이동
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            
            # 맵을 벗어나지 않고, 벽이 아니며, 방문하지 않은 경우
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and maps[nx][ny] == 1:
                visited[nx][ny] = True
                queue.append((nx, ny, distance + 1))
    
    # 목표 지점에 도착할 수 없는 경우
    return -1
