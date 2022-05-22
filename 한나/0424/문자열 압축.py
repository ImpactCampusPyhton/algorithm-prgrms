# 프로그래머스 Lv.2
# https://programmers.co.kr/learn/courses/30/lessons/60057

def solution(s):
    n = len(s)
    answer = n
    
    for i in range(1, n // 2 + 1):
        res = ''
        cnt = 1
        prev = s[: i]
        
        for j in range(i, n, i):
            cur = s[j : j + i]
            if cur == prev:
                cnt += 1
            else:
                if cnt < 2:
                    res += prev
                else:
                    res += str(cnt) + prev
                cnt = 1
                prev = cur
                
        if cnt < 2:
            res += prev
        else:
            res += str(cnt) + prev

        answer = min(answer, len(res))
    
    return answer

print(solution)