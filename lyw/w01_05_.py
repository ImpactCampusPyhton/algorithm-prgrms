#문자열 뒤집기
#0과 1로만 이루어진 문자열 S가 있습니다. 문자열 S에 있는 모든 숫자를 전부 같게 만들려고 합니다.
#문자열S가 주어졌을 때 행동의 최소 횟수 구하세요.
# 입력값 0001100

data = input()
count0 = 0 #전부 0으로 바꾸는경우
count1 = 0 #전부 1로 바꾸는 경우
if data[0] =='1':
    count0 +=1
else:
    count1 +=1
#두번쨰 원소부터 원소 확인
for i in range(len(data) - 1):
    if data[i] != data[i+1]:
        #다음에서 1로 바뀌는 경우
        if data[i+1] =='1':
            count0 +=1
        #다음에서 0으로 바뀌는 경우
        else:
            count1 +=1

print(min(count0,count1))