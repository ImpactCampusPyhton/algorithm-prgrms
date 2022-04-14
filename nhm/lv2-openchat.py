
from contextlib import nullcontext


record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
# ["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."]


def solution(record):
    answer = []
    user = {}

    # 1) {아이디: 닉네임} 형태의 딕셔너리를 만든다. 이때, 동일 닉네임이 있으면 가장 최신으로 변경된다.
    for r in record:
        if r.split()[0] == 'Enter' or r.split()[0] == 'Change':
            user[r.split()[1]] = r.split()[2]
    print(user)
    
    # 2) 1)의 딕셔너리를 참고해 새로운 닉네임이 들어간 텍스트 결과를 출력한다.
    for r in record:
        if r.split()[0] == 'Enter' and user[r.split()[1]]:
            answer.append(user[r.split()[1]]+'님이 들어왔습니다.')
        elif r.split()[0] == 'Leave' and user[r.split()[1]]:
            answer.append(user[r.split()[1]]+'님이 나갔습니다.')

    return answer

print(solution(record))