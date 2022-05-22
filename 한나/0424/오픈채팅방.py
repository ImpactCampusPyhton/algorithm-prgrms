# 프로그래머스 Lv.2
# https://programmers.co.kr/learn/courses/30/lessons/42888

def solution(record):
    answer = []
    dic = dict()
    
    for r in record:
        r = r.split(' ')
        if r[0] in ['Enter', 'Change']:
            dic[r[1]] = r[2]

    for r in record:
        r = r.split(' ')
        if r[0] == 'Enter':
            answer.append('{0}님이 들어왔습니다.'.format(dic[r[1]]))
        elif r[0] == 'Leave':
            answer.append('{0}님이 나갔습니다.'.format(dic[r[1]]))
    
    return answer