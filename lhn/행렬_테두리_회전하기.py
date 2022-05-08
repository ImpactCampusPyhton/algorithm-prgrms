# 프로그래머스 Lv.2
# https://programmers.co.kr/learn/courses/30/lessons/77485

def solution(rows, columns, queries):
    grid = [[0] * columns for _ in range(rows)]
    num = 0
    answer = []
    
    for i in range(rows):
        for j in range(columns):
            num += 1
            grid[i][j] = num
    
    for x1, y1, x2, y2 in queries:
        x1, y1, x2, y2 = x1 - 1, y1 - 1, x2 - 1, y2 - 1
        tmp = grid[x1][y1] # 가장 왼쪽 상단 값
        minimum = grid[x1][y1]
        
        for x in range(x1, x2):
            value = grid[x + 1][y1]
            grid[x][y1] = value
            minimum = min(minimum, value)
        
        for y in range(y1, y2):
            value = grid[x2][y + 1]
            grid[x2][y] = value
            minimum = min(minimum, value)
        
        for x in range(x2, x1, -1):
            value = grid[x - 1][y2]
            grid[x][y2] = value
            minimum = min(minimum, value)
            
        for y in range(y2, y1, -1):
            value = grid[x1][y - 1]
            grid[x1][y] = value
            minimum = min(minimum, value)
            
        grid[x1][y1 + 1] = tmp
        answer.append(minimum)

    return answer

# 참고: https://latte-is-horse.tistory.com/146