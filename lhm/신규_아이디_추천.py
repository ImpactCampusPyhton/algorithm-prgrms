# https://programmers.co.kr/learn/courses/30/lessons/72410?language=python3
import re


def solution(new_id):
    answer = ''
    new_id = new_id.lower()
    for word in new_id:
        if word.isalnum() or word in '-_.':
            answer += word
    while '..' in answer:
        answer = answer.replace('..', '.')
    if answer[0] == '.' and len(answer) > 1:
        answer = answer[1:]
    if answer[-1] == '.':
        answer = answer[:-1]
    if answer == '':
        answer = 'a'
    if len(answer) > 15:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]
    if len(answer) < 3:
        answer = answer + answer[-1] * (3-len(answer))
    return answer


def solution2(new_id):
    st = new_id
    st = st.lower()
    st = re.sub('[^a-z0-9\-_.]', '', st)
    st = re.sub('\.+', '.', st)
    st = re.sub('^[.]|[.]$', '', st)
    st = 'a' if len(st) == 0 else st[:15]
    st = re.sub('^[.]|[.]$', '', st)
    st = st if len(st) > 2 else st + "".join([st[-1] for i in range(3-len(st))])
    return st


if __name__ == '__main__':
    print(solution("...!@BaT#*..y.abcdefghijklm"))
    print(solution2("...!@BaT#*..y.abcdefghijklm"))
