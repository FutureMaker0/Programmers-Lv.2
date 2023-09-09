from itertools import permutations
import math

def is_prime(n):
    # print(result)
    if n <= 1: 
        return False
    else:
        for i in range(2, int(math.sqrt(n)+1)):
            if n % i == 0:
                return False
        return True

def solution(numbers):
    result = set()
    
    for i in range(1, len(numbers) + 1):
        perm = permutations(numbers, i)
        # print(list(perm))
        for p in perm:
            # print(p)
            num = int(''.join(map(str, p)))
            result.add(num) # set으로 해서 중복요소는 알아서 걸러준다.
    print(result)
    
    answer = 0
    for elem in result:
        if is_prime(elem):
            answer += 1
    
    return answer
