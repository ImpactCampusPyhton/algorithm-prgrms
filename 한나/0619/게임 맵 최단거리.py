# 프로그래머스 Lv.2
# https://programmers.co.kr/learn/courses/30/lessons/1844

from collections import deque

def solution(maps):
    n, m = len(maps), len(maps[0])
    q = deque([(0, 0)])
    dist = [[-1] * m for _ in range(n)] #? [[-1] * m] * n 표현식과의 차이
    dist[0][0] = 1          
        
    while q:
        x, y = q.popleft()
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1 and dist[nx][ny] == -1:
                q.append((nx, ny))
                dist[nx][ny] = dist[x][y] + 1
    
    return dist[-1][-1]