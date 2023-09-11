from itertools import product

def solution(word):
    answer = 0
    have = ['A', 'E', 'I', 'O', 'U']
    
    words = []
    for i in range(1, 6):
        for char in product(have, repeat=i):
            words.append(''.join(char))
    
    words.sort()
    # print(words)
    
    return words.index(word) + 1
