# 프로그래머스 Lv.1
# https://programmers.co.kr/learn/courses/30/lessons/92334

def solution(id_list, report, k):
    report = set(report)
    cnt = {p : 0 for p in id_list} # 신고를 당한 횟수
    answer = [0] * len(id_list)
    
    for r in report:
        reporter, reported = r.split()
        cnt[reported] +=  1
    
    for r in report:
        reporter, reported = r.split()
        if cnt[reported] >= k:
            answer[id_list.index(reporter)] += 1
    
    return answer