#모험가 길드
#N명의 모험가에 대한 정보가 주어졌을 때, 여행을 떠날 수 있는 그룹 수의 최대값
# 입력 5
# 입력 2 3 1 2 2
n = int(input())
data = list(map(int, input().split()))
data.sort()
result = 0 #총 그룹스

count = 0 #현재 그룹에 모험가수

for i in data: #공포도 낮은것부터 하나씩
    count += 1 #현재그룹 모험가 추가
    if count >= i: #현재그룹 모험가수가 현재 공포도 이상이면 그룹 결성
        result += 1 #총 그룹수 증가
        count = 0 #현재 그룹 포함된 모험가 수 초기화
print(result)