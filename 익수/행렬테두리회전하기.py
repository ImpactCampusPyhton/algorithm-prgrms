# 행렬 테두리 회전하기
# https://programmers.co.kr/learn/courses/30/lessons/77485
# 참고 : https://roomedia.tistory.com/entry/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%ED%96%89%EB%A0%AC-%ED%85%8C%EB%91%90%EB%A6%AC-%ED%9A%8C%EC%A0%84%ED%95%98%EA%B8%B0-2021-Dev-Matching-%EC%9B%B9-%EB%B0%B1%EC%97%94%EB%93%9C-%EA%B0%9C%EB%B0%9C 
from icecream import ic
from numpy import mat
rows = 6
columns = 6
queries = [[2,2,5,4],[3,3,6,6],[5,1,6,3]]

# creating matrix
matrix = []
temp_list = []
answer = []
for i in range(1, rows + 1):
    for j in range(1, columns + 1):
        temp_list.append((i-1) * columns + j)
    matrix.append(temp_list)
    temp_list=[]
        
# rotation
for t, l, b, r in queries:
    top, left, bottom, right = t - 1, l - 1, b - 1, r - 1
    
    tmp = matrix[top][left]
    min = 2147000000
    
    for y in range(top, bottom): # 서쪽
        matrix[y][left] = matrix[y + 1][left]
        if matrix[y + 1][left] < min:
            min = matrix[y + 1][left]
            
    for x in range(left, right): # 남쪽
        matrix[bottom][x] = matrix[bottom][x + 1]
        if matrix[bottom][x + 1] < min:
            min = matrix[bottom][x + 1]
        
    for y in range(bottom, top, -1): # 동쪽
        matrix[y][right] = matrix[y - 1][right]
        if matrix[y - 1][right] < min:
            min = matrix[y - 1][right]
        
    for x in range(right, left, -1): # 북쪽
        matrix[top][x] = matrix[top][x - 1]
        if matrix[top][x - 1] < min:
            min = matrix[top][x - 1]
        
    matrix[top][left + 1] = tmp
    
    if tmp < min:
        min = tmp
        
    answer.append(min)
    

print(answer)