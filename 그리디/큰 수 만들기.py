# def solution(number, k):
#     stack = []
    
#     for n in number:
#         while k>0 and stack and stack[-1]<n:
#             stack.pop()
#             k -= 1
#         stack.append(n) # while문 종류 후 무조건 실행해야 하는 라인
    
#     answer = stack[:-k] if k>0 else stack
#     return ''.join(answer)


def solution(number, k):
    # stack
    answer = ''
    stack = []
    for n in number:
        # while stack을 걸어주는 것은 맨 처음에 원소 하나를 append 하기 위해서.
        while stack and k>0 and stack[-1] < n:
            stack.pop()
            k -= 1
        
        stack.append(n)
    
    answer = stack[:-k] if k>0 else stack
    return ''.join(answer)
