def solution(record):
    answer = []
    user_list = {}
    for r in record:
        r_split = r.split(" ")
        if len(r_split) == 3:
            _, user_id, name = r.split(" ")
            user_list[user_id] = name
            
    for r in record:
        action, user_id = r.split(" ")[0], r.split(" ")[1]
        if action == 'Enter':
            answer.append(f'{user_list[user_id]}님이 들어왔습니다.')
        elif action == 'Leave':
            answer.append(f'{user_list[user_id]}님이 나갔습니다.')
    
    return answer
