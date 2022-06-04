# lv 2 멀쩡한 사각형

def solution(w,h):
    if w >h:
        square = w
    else:
        square = h
    #print(square)
    for i in range(1, square +1):
        #print(i)
        if w % i == 0 and h % i == 0:

            LCM = i
            #print(LCM)
    return w*h -(w /LCM + h /LCM - 1) * LCM

w = 8
h =12

print(solution(w,h))