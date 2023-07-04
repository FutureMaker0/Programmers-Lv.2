def solution(citations):
    answer = 0
    n = len(citations)
    
    if citations.count(0) == len(citations):
        return 0
    
    result = []
    for h in range(max(citations)):
        yes_in = []
        no_in = []
        # print(f'{h}번 이상 인용된 논문')
        for num in citations:
            if num >= h:
                yes_in.append(num)
            else:
                no_in.append(num)
    
        # print(yes_in)
        result.append(yes_in)
    
    # print(result)
    final = []
    for case in enumerate(result):
        # print(case)
        if case[0] <= len(case[1]):
            final.append(case[0])
    
    answer = max(final)
    return answer
    
    
    '''
    25 8 5 3 3
    0 - 10 8 5 3 3 (5)
    1 - 10 8 5 3 3 (5)
    2 - 10 8 5 3 3 (5)
    3 - 10 8 5 3 3 (5)
    4 - 10 8 5 (3)
    5 - 10 8 5 (3)
    6 - 10 8 (2)
    7 - 10 8 (2)
    8 - 10 8 (2)
    9 - 10 (1)
    10 - 10 (1)
    
    '''



'''
채점 결과
정확성: 100.0
합계: 100.0 / 100.0
'''
