# 리스트를 활용하는 특정 코드를
# 딕셔너리로 변경하여 시간복잡도를 줄인 코드.

def solution(s):
    
    data = sorted(s[2:-2].split('},{'), key=len)
    # print(data)
    
    answer = {} # 시간복잡도 감축
    for tuples in data:
        items = tuples.split(',')
        # print(item)
        for item in items:
            item = int(item)
            # print(item)
            if item not in answer:
                answer[item] = 1

    return list(answer) # 튜플과 리스트 간에는 map 없이 호환된다.

