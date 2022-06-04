def solution(s):
    answer = []
    s = s[2:-2]
    #print(s)
    s = s.split("},{")
    s.sort(key= len)
    #print(s)
    for i in s:
        l = i.split(',')
        #print(l)
        for j in l:
            if int(j) not in answer:
                answer.append(int(j))
    return answer