def solution(p):
    if not p:
        return ''
    u = ''
    v = ''
    count = 0
    inner_count = 0

    for current in p:
        if current == '(':
            count += 1
            u += current
        else:
            count -= 1
            u += current
        if count == 0:
            v = p[len(u):]
            u_right = True
            for inner_u in u:
                if inner_u == '(':
                    inner_count += 1
                else:
                    inner_count -= 1
                if inner_count < 0:
                    u_right = False
            if u_right:
                return u + solution(v)
            else:
                new = ''
                for i in u[1:-1]:
                    if i == '(':
                        new += ')'
                    else:
                        new += '('
                answer = '(' + solution(v) + ')' + new
    return answer

# 참고 : https://this-programmer.tistory.com/384