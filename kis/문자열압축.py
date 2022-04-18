# 문자열 압축
# https://programmers.co.kr/learn/courses/30/lessons/60057

def solution(s):
    result = []
    if len(s) == 1:
        return 1
    
    for num_cut in range(1, (len(s) // 2) + 1):
        cut_string = s[ : num_cut] # 처음 부분
        temp = ''
        cnt = 1
        
        for i in range(num_cut, len(s), num_cut):
            if cut_string == s[i : num_cut + i]:
                cnt += 1
            else:
                if cnt != 1:
                    temp = temp + str(cnt) + cut_string
                else:
                    temp = temp + cut_string
                cut_string = s[i : num_cut + i]
                cnt = 1
                
        if cnt != 1:
            temp = temp + str(cnt) + cut_string
        else:
            temp = temp + cut_string
        
        result.append(len(temp))
        
    return min(result)
        
        
        