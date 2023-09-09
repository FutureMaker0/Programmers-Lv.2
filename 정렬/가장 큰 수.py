'''
from itertools import permutations

def solution(numbers):
    answer = ''
    result = []
    
    for case in permutations(numbers, len(numbers)):
        # print(case)
        for elem in case:
            # print(elem, type(elem))        
            answer += str(elem)
        # print(answer)
        result.append(answer)
        answer = ''
        
    # print(type(result[0]))
    answer = max(result)
        
    return answer
'''

def solution(numbers):
    numbers = list(map(str, numbers)) # 문자열로 변환
    # numbers = list(numbers)
    # print(numbers)
    
    # 문자열을 연결하여 비교하되, 큰 순서대로 정렬
    numbers.sort(key=lambda x: x*7, reverse=True)
    print(numbers)
    
    # 첫 글자가 0일 경우 뒤에도 다 0이므로 리턴 0
    if numbers[0] == '0':
        return '0'
    
    return ''.join(numbers)

