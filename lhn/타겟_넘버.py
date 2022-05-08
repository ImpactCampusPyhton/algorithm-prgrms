# 프로그래머스 Lv.2
# https://programmers.co.kr/learn/courses/30/lessons/43165

def solution(numbers, target):
    answer = 0
    
    def dfs(idx, total):
        nonlocal answer

        if idx == len(numbers):
            if total == target:
                answer += 1
        else:
            dfs(idx + 1, total + numbers[idx])
            dfs(idx + 1, total - numbers[idx])

    dfs(0, 0)
    
    return answer