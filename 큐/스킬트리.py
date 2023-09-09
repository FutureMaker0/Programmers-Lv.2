from collections import deque

def solution(skill, skill_trees):
    answer = 0
    
    for skills in skill_trees:
        skill_list = deque(skill[:])
        
        # 하나라도 브레이크 걸리면 끝
        # 끝까지 브레이크가 안걸리면 answer += 1
        for s in skills:
            if s in skill and s != skill_list.popleft():
                break
        else:
            answer += 1
    
    return answer

