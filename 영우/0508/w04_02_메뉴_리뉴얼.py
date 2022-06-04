import itertools
from collections import Counter

def solution(orders,course):
    answer = []
    max_values = []
    menus = []

    for c in course:
        menu = []

        for order in orders:
            menu_condidate = itertools.combinations(sorted(order),c)
            menu += [ a for a in list(menu_condidate)]
            #print(menu)
        if len(menu)>=1:
            max_values.append(Counter(menu).most_common(1)[0][1])
            menus.append(menu)
            print(max_values.append(Counter(menu).most_common(1)[0][1]))
            #print(menus)

    for max_, menu in zip(max_values, menus):
        #print(max_values)
        #print(menus)
        for key, values in Counter(menu).items():
            #print(Counter(menu).items())
            if max_ == values and values >= 2:
                answer.append("".join(key))


    return sorted(answer)






orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
course= [2,3,4]	#["AC", "ACDE", "BCFG", "CDE"]
# orders = ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]	course = [2,3,5]	#["ACD", "AD", "ADE", "CD", "XYZ"]
# orders = ["XYZ", "XWY", "WXA"]	course =[2,3,4]	#["WX", "XY"]

print(solution(orders,course))