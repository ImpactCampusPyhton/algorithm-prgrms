# lv2 타겟넘버

def solution(numbers,target):
    sum =[0]
    #print(type(sum))

    for i in numbers:
        #print(i)
        re=[]
        for j in sum:
            #print(j)
            print(sum)
            re.append(j+i)
            re.append(j-i)
            #print(type(re))


        #print(re)
        sum = re
        #print(type(sum))
        # print(sum)
        # print(re)
    return sum.count(target)

numbers = [1,1,1,1,1]
target = 3
print(solution(numbers,target))