# 프로그래머스 Lv.2
# https://programmers.co.kr/learn/courses/30/lessons/12899

def solution(n):
    answer = ''
    
    nums = [1, 2, 4]
    
    while n > 0:
        n -= 1
        answer = str(nums[n % 3]) + answer
        n //= 3
    
    return answer

# 참고: https://velog.io/@eerang/PYTHON-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4Level2-124%EB%82%98%EB%9D%BC%EC%9D%98-%EC%88%AB%EC%9E%90