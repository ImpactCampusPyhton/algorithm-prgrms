# 프로그래머스 Lv.2
# https://programmers.co.kr/learn/courses/30/lessons/67257

import re
from itertools import permutations

def solution(expression):
    expression = re.split('([-+*])', expression)
    operators = list(permutations('-+*', 3))
    results = []
    
    for operator in operators:
        exp = expression[:]
        for op in operator:
            while op in exp:
                idx = exp.index(op)
                exp[idx - 1] = str(eval(exp[idx - 1] + op + exp[idx + 1]))
                del exp[idx:idx + 2]
        results.append(abs(int(exp[0])))
    
    return max(results)