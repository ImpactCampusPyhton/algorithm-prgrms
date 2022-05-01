# 짝지어 제거하기
# https://programmers.co.kr/learn/courses/30/lessons/12973


# try1
# def solution(s):
#     s = list(s)
#     for k in range(len(s)//2):
#         cnt = 0	
#         for i in range(len(s)-1):
#             if s[i] == s[i + 1]:
#                 s.pop(i - cnt + 1)
#                 s.pop(i - cnt)
#                 cnt += 2
#                 if len(s) <= i:
#                     break
#         if s == []:
#             answer = 1
#         else:
#             answer = 0
#     return answer


# try2
# 시간초과

# s = "baabaa"
# s = list(s)

# tmp = 0

# while(1):
#     if s[tmp] == s[tmp + 1]:
#         s.pop(tmp + 1)
#         s.pop(tmp)
#         tmp = 0
#     else:
#         tmp += 1
        
#     if s == []:
#         answer = 1
#         break;
#     elif tmp == len(s) - 1:
#         answer = 0
#         break;
# print(answer)

# try3

s = "baabaa"
s = list(s)

stack = []

for i in s:
    if len(stack) == 0:
        stack.append(i)
    elif stack[-1] == i:
        stack.pop()
    else:
        stack.append(i)
        
if len(stack) == 0:
    answer = 1
else:
    answer = 0
    
    