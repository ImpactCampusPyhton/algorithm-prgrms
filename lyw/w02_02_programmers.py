# lv2 타겟 넘버
#BFS 탐색을 이용
def solution(numbers, target):
    sub = [0]
    for i in numbers:
        ss = []
        for j in sub:
            ss.append(j+i)
            ss.append(j-i)
        sub = ss
        #print(ss)
    #print(sub)
    #print(ss)

    return sub.count(target)


numbers = [1, 1, 1, 1, 1]
target = 3
#numbers = [4, 1, 2, 1]
#target = 4
#solution(numbers,target)
print(solution(numbers,target))

