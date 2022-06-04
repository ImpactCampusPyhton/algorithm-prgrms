places = \
    [
        ["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], \
        ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], \
        ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], \
        ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], \
        ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]
    ]
#	[1, 0, 1, 1, 1]


# 찾은 풀이 - bfs
## 참고: https://hbj0209.tistory.com/136
from collections import deque
def solution(places): 
    dx, dy = [0,0,-1,1], [-1,1,0,0]
    def bfs(i, j, m, visited):
        q.append((i, j))
        visited[i][j] = True
        while q:
            x, y = q.popleft()
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < 5 and 0 <= ny < 5 and n[nx][ny] != 'X' and not visited[nx][ny]:
                    m[nx][ny] = m[x][y] + 1
                    q.append((nx, ny))
                    visited[nx][ny] = True
        return m
 
    answer = []
    for n in places:
        p = []
        tf = False
        for i in range(5):
            for j in range(5):
                if n[i][j] == 'P':
                    p.append([i, j])      
        
        for i, j in p:
            m = [[0] * 5 for _ in range(5)]
            q = deque()
            visited = [[False] * 5 for _ in range(5)]
            dist = bfs(i, j, m, visited)
            for cx, cy in p:
                if (cx, cy) != (i, j) and 1 <= dist[cx][cy] <= 2:
                    answer.append(0)
                    tf = True
                    break
            if tf:
                break
        if not tf:
            answer.append(1)
            
    return answer

