def solution(s):
    stack = []
    
    for elem in s:
        if stack and stack[-1] == elem:
            stack.pop()
        else:
            stack.append(elem)
    
    if stack:
        return 0
    else:
        return 1



'''
채점 결과
정확성: 60.2
효율성: 39.8
합계: 100.0 / 100.0    
'''    
