from collections import defaultdict

def solution(id_list, report, k):
    answer = [0] * len(id_list)
    report = set(report)
    
    report_dict = defaultdict(set)
    count_dict = defaultdict(int)
    result = []
    
    for r in report:
        user_id, reported_id = r.split(" ")
        
        count_dict[reported_id] += 1 
        report_dict[user_id].add(reported_id)
        
        if count_dict[reported_id] == k:
            result.append(reported_id)
            
    for reported_user in result:
        for idx, user in enumerate(id_list):
            if reported_user in report_dict[user]:
                answer[idx] += 1
    return answer
