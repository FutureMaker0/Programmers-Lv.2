# 스택에서는 넣고 조건에 부합하면 바로바로 삭제.
# 줄이고 줄여서 최종 목표에 부합을 하면 true.
# 부합하지 않으면 false 를 리턴.
# 괄호 문제는 무조건 스택 문제이다.

def solution(s):
    stack = []
    cnt = 0
    
    for elem in s:
        if elem == '(':
            stack.append(elem)
        elif elem == ')':
            if not stack:
                return False
            stack.pop()
    
    # print(len(stack) == 0)
    
    # 리턴 안의 조건문 참거짓 여부를 판단하여 true/false를 리턴할 수 있다.
    # return len(stack) == 0

    if not stack:
        return True
    elif len(stack) >= 1:
        return False
    
    
