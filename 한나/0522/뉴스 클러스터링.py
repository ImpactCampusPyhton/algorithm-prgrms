# 프로그래머스 Lv.2
# https://programmers.co.kr/learn/courses/30/lessons/17677

def solution(str1, str2):
    answer = 0
    str1, str2 = str1.upper(), str2.upper()
    s1, s2 = [], []
    
    # 집합 구하기
    for i in range(len(str1) - 1):
        s = str1[i:i + 2]
        if s.isalpha():
            s1.append(s)
    for i in range(len(str2) - 1):
        s = str2[i:i + 2]
        if s.isalpha():
            s2.append(s)
    
    # 두 집합 모두 공집합일 경우
    if len(s1) == 0 and len(s2) == 0:
        return 65536

    # 자카드 유사도 구하기
    intersection, union = 0, 0
    for s in set(s1 + s2):
        intersection += min(s1.count(s), s2.count(s))
        union += max(s1.count(s), s2.count(s))
        
    return int(intersection / union * 65536)