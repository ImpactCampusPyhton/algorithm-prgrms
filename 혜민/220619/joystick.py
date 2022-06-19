# 조이스틱 

def solution(name):
    answer = 0
    min_name = [min(ord(i) - ord('A'), ord('Z') - ord(i) + 1) for i in name]
    print(min_name)

    # A 위치 확인
    idx = 0
    while True:
        answer += min_name[idx]
        min_name[idx] = 0
        if sum(min_name) == 0:
            break
        
        left,right = 1,1
        while min_name[idx - left] == 0:
            left += 1
        while min_name[idx + right] == 0:
            right += 1
        
        answer += left if left < right else right
        idx += -left if left < right else right
    return answer