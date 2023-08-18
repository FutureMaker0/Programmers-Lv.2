# 뭔지 모르겠으나 일단 제출

'''    
['Jeju'] # 5
['Jeju', 'Pangyo'] # 5
['Jeju', 'Pangyo', 'Seoul'] # 5
['Pangyo', 'Seoul', 'NewYork'] # 5
['Seoul', 'NewYork', 'LA'] # 5
['NewYork', 'LA', 'Seoul'] # 1
# ...
'''

from collections import deque

def solution(cacheSize, cities):
    
    l = [''] * cacheSize #1차원 곱하기는 상관 없다.
    cache = deque(l, maxlen=cacheSize) # 길이 제한
    answer = 0 # 시간
    # print(cache)

    for city in cities:
        city = city.lower()
        if city in cache: # cache hit
            cache.remove(city)
            cache.append(city)
            answer += 1
        else: # cache miss
            cache.append(city)
            answer += 5
    
    # cache.append('hello')
    # cache.append('hello')
    # cache.append('hello')
    # cache.append('hello') # maxlen까지만 append 된다.

    return answer
    
