grid1 = ["SL","LR"]	 # [16]
grid2 = ["S"] # [1,1,1,1]
grid3 = ["R","R"] # [4,4]

# 찾은 풀이 - dfs 해석 필요 ★★
# 참고 : https://studyandwrite.tistory.com/435

dx, dy = [-1,0,1,0],[0,1,0,-1]
def lightRoute(grid, visited, i, j, k):
   r, c = len(grid), len(grid[0])
   route = 1
   # 나가는 경로 체크
   visited[i][j][k] = True
   # 처음 방문한 노드 (ni, nj) = 다음 지점이면서 범위를 벗어나는 경우를 고려한다.
   nx, ny = (i + dx[k]) % r, (j + dy[k]) % c
 
   # 이제부터 이미 방문한 경로를 만나면 끝
   while True:
       # 직진 = 현재 방향 그대로 유지
       if grid[nx][ny] == 'S': pass
       # 좌회전 = (현재 진행 방향 - 1) % 4
       elif grid[nx][ny] == 'L': k = (k-1) % 4  
       # 우회전 = (현재 진행 방향 + 1) % 4
       elif grid[nx][ny] == 'R': k = (k+1) % 4           
 
       # 방문하지 않은 경로라면 길이를 1 증가시키고 방향 전환
       if not visited[nx][ny][k]:
           route += 1
           visited[nx][ny][k] = True
           nx, ny = (nx + dx[k]) % r, (ny + dy[k]) % c
       else:
           return route
 
def solution(grid):
   answer = []
   r, c = len(grid), len(grid[0])
   # 모든 격자점을 시작점으로 네 방향으로 빛을 진행시켜본다.
   # 북동남서(시계방향)로 나가는 경로를 체크하는 리스트
   visited = [[[False] * 4 for _ in range(c)] for _ in range(r)]
   for i in range(r):
       for j in range(c):
           for k in range(4):
                # 해당 지점에서 나가는 경로는 무조건 같은 싸이클을 형성
                if visited[i][j][k]:continue
                answer.append(lightRoute(grid, visited, i, j, k))
   return sorted(answer)

print(solution(grid1))
# solution(grid1)