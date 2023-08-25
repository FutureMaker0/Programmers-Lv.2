def solution(number, k):
    stack = []
    
    for n in number:
        while k>0 and stack and stack[-1]<n:
            stack.pop()
            k -= 1
        stack.append(n) # while문 종류 후 무조건 실행해야 하는 라인
    
    answer = stack[:-k] if k>0 else stack
    return ''.join(answer)

