# 프로그래머스 Lv.2
# https://programmers.co.kr/learn/courses/30/lessons/12973

def solution(s):
    stack = []
    answer = 0
    
    for x in s:
        if stack:
            if stack[-1] == x:
                stack.pop()
            else:
                stack.append(x)
        else:
            stack.append(x)
    
    if not stack:
        answer = 1
        
    return answer