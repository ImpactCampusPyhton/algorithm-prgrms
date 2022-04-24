def cal_gcd(w, h):
    a, b = max([w, h]), min([w, h])
    while True:
        if a % b == 0:
            return b
        a, b = b, a % b

def solution(w, h):
    squares = w * h
    gcd = cal_gcd(w, h)
    return squares - (w + h - gcd)
