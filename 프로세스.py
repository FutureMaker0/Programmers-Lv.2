from collections import deque

'''
2 1 3 3 - 3

1 3 3 2 - 2
3 3 2 1 - 1
answer = 2
idx = 0
'''

def solution(priorities, location):
    answer = 1
    q = deque(priorities)
    # print(q)
    idx = location
    # print(idx)
    
    while len(q)>1: # 덱의 내용물이 있는 동안 
        temp = q.popleft() # 덱의 첫 번째 요소
        # print(temp)
        
        if temp < max(q): # 꺼낸 값이 덱 내 최댓값보다 작으면
            q.append(temp) # 일단 덱 끄트머리에 값을 넣는다.
            # print(q)
            
            if idx == 0: 
                # 맨 처음에 있는 거엿으면 맨 뒤로 돌아가서 붙었기 때문에
                # 인덱스를 맨 뒤로 바꿔주고
                idx = len(q)-1
            else:
                idx -= 1 # 맨 뒤 요소가 아니면 한칸 앞으로 당겨준다
                
        else: # 꺼낸 값이 덱 내 최댓값과 크거나 같은 상황에서,
            
            if idx == 0: # 맨 앞에 있떤 값이라면 
                return answer # 그냥 1을 리턴
            
            else: # 맨 앞에 있는 값은 아니라면
                answer += 1 
                idx -= 1
                
    return answer



'''
채점 결과
정확성: 100.0
합계: 100.0 / 100.0
'''
