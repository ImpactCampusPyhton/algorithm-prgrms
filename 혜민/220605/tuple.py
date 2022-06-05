# 내 풀이 - split함수
def my_solution(s):
    answer = list()
    split_s = list()
    
    # 구분 문자 ",{" 로 문자열 나누고
    s = s.split(",{")
    # "{" 와 "}" 문자 제거하기
    for i in s:
        i = i.replace("{", "")
        i = i.replace("}", "")
        split_s.append(i)
    # 요소 길이로 리스트 정렬하기
    split_s = sorted(split_s, key=lambda x: len(x))

    # 위에서 쪼갠 리스트를 돌면서
    for tuple in split_s:
        # 각 요소를 ,로 구분한 뒤
        numbers = tuple.split(",")
        # 중복된 값이 없도록 결과값 반환
        for number in numbers:
            if int(number) not in answer:
                answer.append(int(number))
    return answer


# 다른 풀이 - 정규표현식
import re 

def solution(s):
    answer = list()
    split_s = list()
    
    # 구분 문자 ",{" 로 문자열 나누기
    split_s = s.split(",{")
    split_s = sorted(split_s, key=lambda x: len(x))

    for tuple in split_s:
        # 숫자(\d) 1개 이상(+) 만 찾기
        numbers = re.findall("\d+", tuple)
        for number in numbers:
            if int(number) not in answer:
                answer.append(int(number))
    return answer