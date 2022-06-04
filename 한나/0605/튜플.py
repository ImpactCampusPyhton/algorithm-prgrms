# 프로그래머스 Lv.2
# https://programmers.co.kr/learn/courses/30/lessons/64065

def solution(s):
    answer = []
    s = sorted(s[2:-2].split('},{'), key = len)
    
    for c in s:
        c = c.split(',')
        for i in c:
            num = int(i)
            if num not in answer:
                answer.append(num)
    
    return list(answer)