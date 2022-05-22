# 신고 결과 받기
# https://programmers.co.kr/learn/courses/30/lessons/92334

def solution(id_list, report, k):
    report = set(report)
    reporter_list = []
    reported_list = []
    banned_list = []
    
    # answer = []    
    result = [0] * len(id_list)
    
    for i in report:
        reporter, reported = i.split()
        reporter_list.append(reporter)
        reported_list.append(reported)

    for id in id_list:
        if reported_list.count(id) >= k: 
            banned_list.append(id)
            
    # for id in id_list:
    #     cnt = 0
    #     for j in report:
    #         reporter, reported = j.split()
    #         if reporter == id and reported in banned_list:
    #             cnt += 1
    #     answer.append(cnt)

    for i in report:
        reporter, reported = i.split()
        if reported in banned_list:
            result[id_list.index(reporter)] += 1

    # return answer
    return result