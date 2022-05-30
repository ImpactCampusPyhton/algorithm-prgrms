# 튜플 
# https://github.com/ImpactCampusPyhton/algorithm-prgrms
from icecream import ic

def solution(s):
    answer = []
    s = s[2:-2].split('},{')
    s = sorted(s, key=len)
    s = [item.split(',') for item in s]
    answer.append(int(s[0][0]))

    for i in range(len(s) - 1):
        first = set(s[i])
        second = set(s[i+1])
        cur_answer = second - first
        cur_answer = int(list(cur_answer)[0])
        answer.append(cur_answer)
    return answer


s = "{{4,2,3},{3},{2,3,4,1},{2,3}}"
print(solution(s))