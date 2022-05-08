# lv2 124 나라의 숫자

def solution(n):
    answer = ''
    while n:
        if n % 3:
            answer += str(n%3)
            print("if:",answer)
            n //= 3 # //= 왼쪽 변수에서 오른쪽 값을 나눈 몫의 결과를 왼쪽변수에 할당
        else:
            answer +="4"
            print("else: ",answer)
            n = n//3 -1
            #print(n)

            #print(answer)
    return answer[::-1]

n =6

print(solution(n))
