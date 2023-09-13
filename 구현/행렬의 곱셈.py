def solution(arr1, arr2):
    
    # 초기화
    answer = [[0 for _ in range(len(arr2[0]))] for _ in range(len(arr1))]
          
    for i in range(len(arr1)):
        for j in range(len(arr2[0])):
            for k in range(len(arr1[0])): # len(arr2[0])으로 하면 런타임 에러
                answer[i][j] += (arr1[i][k] * arr2[k][j])
                
    return answer

'''
    arr1 = [
        1 4
        3 2
        4 1
    ]
    
    arr2 = [
        3 3
        3 3
    ]
    
    '''


'''
채점 결과
정확성: 100.0
합계: 100.0 / 100.0
'''
