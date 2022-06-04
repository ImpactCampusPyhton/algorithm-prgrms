from itertools import permutations
# permutations 반복 가능 객체 중에서 r개를 선택한 순열을 반환하는 함수

def operation(num1, num2, op):
    if op == '+':
        return str(int(num1) + int(num2))
    if op == '-':
        return str(int(num1) - int(num2))
    if op == '*':
        return str(int(num1) * int(num2))


def cal(exp, op):
    array = []
    tmp = ""
    for i in exp:
        if i.isdigit() == True: # isdigit 문자열이 '숫자'로만 이루어져있는지 확인하는 함수
            tmp += i
        else:
            array.append(tmp)
            array.append(i)
            tmp = ""
        print(array)
    array.append(tmp)

    for j in op:
        stack = []
        while len(array) != 0:
            tmp = array.pop(0)
            if tmp == j:
                stack.append(operation(stack.pop(), array.pop(0), j))
            else:
                stack.append(tmp)
        array = stack
    return abs(int(array[0]))


def solution(expression):
    op = ['*', '+', '-']
    op = list(permutations(op, 3))
    result = []
    for i in op:
        result.append(cal(expression, i))
    return max(result)