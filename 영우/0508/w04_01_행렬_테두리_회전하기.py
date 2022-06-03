def solution(rows, columns, queries):
    answer = []
    matrix = [[0 for i in range(columns+1)] for j in range(rows+1)]
    #print(matrix)
    num  = 1
    for row in range(1, rows+1):
        for column in range(1,columns+1):
            matrix[row][column] = num
            num +=1
            #print(row)
            #print(column)
            #print(num)

    for x1, y1, x2, y2 in queries:
        matrix_2 = matrix[x1][y1]
        s_box = matrix_2

        for k in range(x1,x2):
            test= matrix[k+1][y1]
            matrix[k][y1] = test
            s_box = min(s_box, test)
            #print(s_box)

        for k in range(y1,y2):
            test = matrix[x2][k+1]
            matrix[k][y1] = test
            s_box = min(s_box,test)

        for k in range(x2,x1,-1):
            test = matrix[k-1][y2]
            matrix[k][y2] = test
            s_box = min(s_box,test)

        for k in range(y2,y1, -1):
            test = matrix[x1][k-1]
            matrix[x1][k] = test
            mini = min(s_box, test)

        matrix[x1][y1+1] =matrix_2
        answer.append(s_box)

    return answer


rows =6
columns =6
queries = [[2,2,5,4],[3,3,6,6],[5,1,6,3]]	#[8, 10, 25]
# rows =3	columns =3	queries = [[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]]	#[1, 1, 5, 3]
# rows =100	columns =97	queries = [[1,1,100,97]] #[1]

print(solution(rows,columns, queries))
# 출처: https://velog.io/@evencoding/파이썬-프로그래머스-Lv.2-행렬-테두리-회전하기