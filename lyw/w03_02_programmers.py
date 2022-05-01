#lv2 짝지어 제거하기
def solution(s):
    stack = []

    for i in s:
        if len(s) == 0:
            stack.append(i)
        elif stack[-1] == i:
            stack.pop()
        else:
            stack.append(i)

    if len(stack) == 0:
        return 1
    else:
        return 0

s='baabaa'
result = 1
#s='cdcd'
#result = 0
print(solution(s))