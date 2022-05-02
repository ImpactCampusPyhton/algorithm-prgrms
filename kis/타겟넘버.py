# 타겟 넘버
# https://programmers.co.kr/learn/courses/30/lessons/43165

# try
# numbers = [1, 1, 1, 1, 1]
# numbers = [4,1,2,1]
# target = 4
# len_num = len(numbers)
# count = 0
# def DFS(L, sum):
#     global count
#     if L == len_num:
#         if sum == target:
#             count += 1
#         return 
#     else:
#         DFS(L + 1, sum + numbers[L])
#         DFS(L + 1, sum - numbers[L])

# DFS(0,0)
# print(count)

# try => def
# 최종

count = 0
def solution(numbers, target):
    global count
    len_num = len(numbers)
    count = 0
    
    def DFS(L, sum):
        global count
        if L == len_num:
            if sum == target:
                count += 1
            return 
        else:
            DFS(L + 1, sum + numbers[L])
            DFS(L + 1, sum - numbers[L])
            
    DFS(0,0)
    return count



