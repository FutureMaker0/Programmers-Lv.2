def solution(progresses, speeds):
    answer = []
    
    '''
    while progresses:
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
            
        cnt = 0
        while progresses and progresses[0] >= 100:
            progresses.pop(0)
            speeds.pop(0)
            cnt += 1
        
        if cnt > 0 :
            answer.append(cnt)
            
    return answer
    '''
    
    for progress, speed in zip(progresses, speeds):
        # print(progress, speed)
        if (100 - progress) % speed == 0:
            rest_day = (100 - progress) // speed
        else:
            rest_day = (100 - progress) // speed + 1
        # print(rest_day)
        
        if not answer or answer[-1][0] < rest_day:
            answer.append([rest_day, 1])
        else: answer[-1][1] += 1
    # print(answer)
        
    return [a[1] for a in answer]



'''
채점 결과
정확성: 100.0
합계: 100.0 / 100.0
'''
