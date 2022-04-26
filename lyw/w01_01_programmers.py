# lv2. 문자열 압축

def solution(s):
    answer = 10000
    for i in range(1,len(s)//2+2):
        res = ''
        cnt=1
        tmp=s[:i]

        for j in range(i, len(s)+i,i):
            if tmp ==s[j:j+i]:
                cnt+=1
            else:
                if cnt==1:
                    res+=tmp
                else:
                    res+=str(cnt)+tmp
                tmp=s[j:j+i]
                cnt=1
        print(res)
        answer = min(answer,len(res))
    return answer


s=('aaabbbbbcccccddd')
print(solution(s))