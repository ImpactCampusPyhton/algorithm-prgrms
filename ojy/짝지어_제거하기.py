def solution(s):
    stack = []

    for word in s:
        if stack and stack[-1] == word:
            stack.pop()
        else:
            stack.append(word)
    
    return int(stack == [])
            