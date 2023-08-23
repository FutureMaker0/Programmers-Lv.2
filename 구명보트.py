# 투포인터 

def solution(people, limit):
    answer = 0
    people.sort(reverse=True)
    # print(people) 
    # 80 70 30 30 30
    # 80 70 50 50
    # 80 70 50
    
    left, right = 0, len(people) - 1
    
    while left <= right:
        if people[left] + people[right] <= limit:
            right -= 1  # 두 명을 태우고, 오른쪽 인덱스를 감소시킴
        
        left += 1  # 왼쪽 인덱스는 항상 증가
        answer += 1
    
    return answer
