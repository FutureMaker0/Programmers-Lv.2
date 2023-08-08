from heapq import heapify, heappop, heappush

def solution(scoville, K):
    answer = 0
    heapify(scoville)
    
    while scoville[0] < K and len(scoville) > 1:
        num1 = heappop(scoville)
        num2 = heappop(scoville)
        heappush(scoville, num1 + (num2*2))
        answer += 1
        
    if scoville[0] >= K:
        return answer
    return -1


'''
채점 결과
정확성: 83.9
효율성: 16.1
합계: 100.0 / 100.0
'''
