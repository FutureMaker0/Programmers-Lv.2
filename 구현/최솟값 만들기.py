# 1번 배열 최솟값
# 2번 배열 최댓값
# 곱 누적값이 전체 최솟값

def solution(A,B):
    answer = 0

    A.sort()
    B.sort(reverse=True)
    
    for i in range(len(A)):
        answer += A[i] * B[i]
    
    return answer
