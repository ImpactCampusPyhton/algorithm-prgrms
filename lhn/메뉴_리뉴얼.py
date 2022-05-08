# 프로그래머스 Lv.2
# https://programmers.co.kr/learn/courses/30/lessons/72411

from itertools import combinations

def solution(orders, course):
    menu = {c:{} for c in course}
    answer = []

    # 코스 > 세트 별 세트 이름과 주문 횟수 등록
    for o in orders:
        for c in course:
            for comb in list(combinations(sorted(o), c)):
                comb = ''.join(comb)
                menu[c][comb] = menu[c].get(comb, 0) + 1
    
    # 각 코스 조회
    for course in menu.values():
        maximum = 0
        # 세트 중 최대 주문 횟수 구하기
        for c in course.values():
            maximum = max(maximum, c)
        # 주문 횟수가 2번 이상이고, 최대 주문 횟수에 해당하는 세트 이름 구하기
        for k, v in course.items():
            if maximum >= 2 and v == maximum:
                answer.append(k)
    
    return sorted(answer)