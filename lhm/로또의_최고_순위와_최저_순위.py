# https://programmers.co.kr/learn/courses/30/lessons/77484#fnref1

def solution(lottos, win_nums):
    answer = []
    undefined = 0
    winning = 0
    for lotto in sorted(lottos):
        if lotto in win_nums:
            winning += 1
        if lotto == 0:
            undefined += 1
    highest = 7 - (undefined + winning)
    lowest = 7 - winning
    if highest >= 6:
        highest = 6
    if lowest >= 6:
        lowest = 6
    answer.append(highest)
    answer.append(lowest)
    return answer


def solution2(lottos, win_nums):

    rank = [6, 6, 5, 4, 3, 2, 1]

    cnt_0 = lottos.count(0)
    ans = 0
    for x in win_nums:
        if x in lottos:
            ans += 1
    return rank[cnt_0 + ans], rank[ans]


if __name__ == '__main__':
    # print(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]))
    print(solution2([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]))
