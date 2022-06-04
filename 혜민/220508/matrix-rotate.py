def solution(rows, columns, queries):

    # 행렬 만들기
    matrix = [[i * columns + (j+1) for j in range(columns)] for i in range(rows)]
    answer = []
    
    # queries 배열 분리: 인덱스 0부터 시작하도록 변경
    for x1, y1, x2, y2 in queries:
        x1, y1, x2, y2 = x1-1, y1-1, x2-1, y2-1
        # 특정 자리 수를 임시저장: (x1, y1) = (맨 위의, 맨 왼쪽)
        temp = matrix[x1][y1]
        min_value = temp

        # 맨 위 행: (x1 ~ x2) = (왼쪽 끝 ~ 오른쪽 끝)
        for x in range(x1, x2):
            # 시계방향 회전 -> x행 오른쪽 방향으로 한칸씩 증가
            matrix[x][y1] = matrix[x+1][y1] 
            # 임시저장값과 변경된 값 중 최소값 찾기 
            min_value = min(min_value, matrix[x+1][y1])

        # 맨 오른쪽 열: (y1 ~ y2) = (맨 위 ~ 맨 아래)
        for y in range(y1, y2):
            # 시계방향 회전 -> y열 아래 방향으로 한칸씩 증가
            matrix[x2][y] = matrix[x2][y+1] 
            # 임시저장값과 변경된 값 중 최소값 찾기 
            min_value = min(min_value, matrix[x2][y+1])
        
        # 맨 아래 행: (x2 ~ x1) = (맨 오른쪽 ~ 맨 왼쪽)
        for x in range(x2, x1, -1):
            # 시계방향 회전 -> x행 역방향인 왼쪽으로 한칸씩 감소
            matrix[x][y2] = matrix[x-1][y2] 
            # 임시저장값과 변경된 값 중 최소값 찾기 
            min_value = min(min_value, matrix[x-1][y2])
        
        # 맨 왼쪽 열: (y2 ~ y1) = (맨 아래 ~ 맨 위)
        for y in range(y2, y1+1, -1):
            # 시계방향 회전 -> y열 역방향인 위쪽으로 한칸씩 감소
            matrix[x1][y] = matrix[x1][y-1] 
            # 임시저장값과 변경된 값 중 최소값 찾기 
            min_value = min(min_value, matrix[x1][y-1])
        
        # 임시저장한 값 회전시키기
        matrix[x1][y1+1] = temp
        
        # 최종 최소값 출력
        answer.append(min(min_value, temp))

    return answer


'''
참고
- https://2hs-rti.tistory.com/entry/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-Lv2-%ED%96%89%EB%A0%AC-%ED%85%8C%EB%91%90%EB%A6%AC-%ED%9A%8C%EC%A0%84%ED%95%98%EA%B8%B0-%ED%8C%8C%EC%9D%B4%EC%8D%AC
- https://roomedia.tistory.com/entry/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%ED%96%89%EB%A0%AC-%ED%85%8C%EB%91%90%EB%A6%AC-%ED%9A%8C%EC%A0%84%ED%95%98%EA%B8%B0-2021-Dev-Matching-%EC%9B%B9-%EB%B0%B1%EC%97%94%EB%93%9C-%EA%B0%9C%EB%B0%9C
'''
