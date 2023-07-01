# dp - 중복적으로 발생하는 호출을 기록하여 두 번 이상 연산하지 않도록 조치.

'''
def fibo(n):
    if n<3: return 1
    return fibo(n-1) + fibo(n-2)

def solution(n):
    return fibo(n) % 1234567
'''
'''
import sys
sys.setrecursionlimit(200000)

def fibo(n, answer):
    if n<2: return 1
    if answer[n] == 0:
        answer[n] = fibo(n-1, answer) + fibo(n-2, answer)

    return answer[n]
        
def solution(n):
    # 크기가 n인 배열 생성
    answer = [0] * n
    answer[0] = answer[1] = 1
    fibo(n-1, answer)
    
    return answer[-1] % 1234567
'''

def solution(n):
    a, b = 1, 1
    for i in range(1, n):
        a, b = b, a+b
    
    return a % 1234567



'''
채점 결과
정확성: 100.0
합계: 100.0 / 100.0
'''
