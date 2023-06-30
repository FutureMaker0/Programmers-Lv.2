# 시간 복잡도의 개념... 효율적인 풀이 방식...

def solution(s):
    answer = ''
    prev_ch = ' '
    
    for elem in s:
        if prev_ch == ' ':
            answer += elem.upper()
        else:
            answer += elem.lower()
        
        prev_ch = elem

    return answer



'''
채점 결과
정확성: 100.0
합계: 100.0 / 100.0
'''
