# 곱하기 혹은 더하기
#숫자 0 부터 9로만 이루어진 문자열 S가 주어졌을 때, 왼쪽 부터 오른쪽으로 하나씩
#숫자를 확인하며 숫자사이에 'x'혹은 '+' 연산자를 넣어 결과적으로 만들어질 수 있는 가장 큰 수 만들어라
# 입력값 02984
# 입력값 567

data = input()
result = int(data[0]) #첫 번쨰 문자를 숫자로 변경
for i in range(1, len(data)):
    # 두 수중에 0 혹은 1인 경우 곱하기보다는 더하기 수행
    num = int(data[i])
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num
print(result)
