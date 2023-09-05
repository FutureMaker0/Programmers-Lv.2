## BFS - deque 사용
from collections import deque

def solution(numbers, target):
    answer = 0
    init_idx = 0
    
    dq = deque()
    dq.append([numbers[0], init_idx])
    dq.append([-1*numbers[0], init_idx])
    
    while dq:
        temp, idx = dq.popleft()
        
        idx += 1
        if idx < len(numbers):
            dq.append([temp + numbers[idx], idx])
            dq.append([temp - numbers[idx], idx])
        else:
            if temp == target:
                answer += 1
                
    return answer
    
    
    

#     answer = 0
#     init_idx = 0
#     q = deque()
#     q.append([numbers[0], init_idx])
#     q.append([-1*numbers[0], init_idx])
    
#     while q:
#         # print(q)
#         temp, idx = q.popleft()
#         # print(temp, idx)
        
#         # 팝한 상태의 인덱스가 매번 새로 나오므로 초기화 하는 것과 유사한 동작이 된다.
#         # 팝한 상태에서 +1 상태로 계속 저장되는 것.
#         idx += 1
#         if idx < len(numbers):
#             # print(numbers[idx], -1*numbers[idx], f'idx={idx}')
#             q.append([temp + numbers[idx], idx])
#             q.append([temp - numbers[idx], idx])
#             # 각 값들이 자신의 인덱스를 함께 가지고 저장되는 것이다.
#         else:
#             # print(temp, idx)
#             if temp == target:
#                 answer += 1
                
#     return answer
