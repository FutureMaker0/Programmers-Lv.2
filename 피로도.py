from itertools import permutations

def solution(k, dungeons):
    possibles = list(permutations(dungeons, len(dungeons)))
    
    visited = []
    for possible in possibles:
        # print(possible)
        stamina = k
        cnt = 0
        for elem in possible:
            # print(elem)
            if elem[0] <= stamina and elem[0] >= elem[1]:
                stamina -= elem[1]
                cnt += 1
                # print(stamina, cnt)
                
        visited.append(cnt)
        # print(visited)
        # print(' ')
    
    return max(visited)
    
    
