# lv2 기능개발

def solution(progresses, speeds):
    answer = []
    days = 1
    counts = 0

    for i in range(len(progresses)):
        if i == 0 and progresses[i] + days * speeds[i] >= 100:
            counts += 1
            answer.append(counts)


        elif i > 0 and progresses[i] + days * speeds[i] >= 100:
            counts += 1
            answer[-1] += 1

        while progresses[i] + days * speeds[i] <100:
            days +=1
            if progresses[i] + days * speeds[i] >=100:
                counts =1
                print(counts)
                answer.append(counts)
                break


    return answer

progress = [93, 30, 55]
speeds = [1, 30, 5]

print(solution(progress,speeds))