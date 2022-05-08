# 메뉴 리뉴얼
# https://programmers.co.kr/learn/courses/30/lessons/72411

import collections
import itertools
from icecream import ic

orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
course = [2, 3, 4]

def solution(orders, course):
    answer = []
    
    for course_size in course:
        order_combinations = []
        for order in orders:
            order_combinations += itertools.combinations(sorted(order), course_size)
        
        most_orderd = collections.Counter(order_combinations).most_common()
        ic(most_orderd)
    
    
    return answer


solution(orders, course)