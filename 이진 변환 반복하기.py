import re

def solution(s):
    cnt = 0
    zero_removed = 0
    while len(s) > 1:
        init_len = len(s)
        s = re.sub('0','', s)
        after_len = init_len - len(s)
        # print(s, after_len)
        zero_removed += after_len

        s = len(s)
        s = bin(s)[2:]
        # print(s)
        cnt += 1
    
    return [cnt, zero_removed]

'''
0111010
1111 길이:4
길이4를 이진법으로 표현 100

110010101001
111111
110 - 1번, 0 6개 제거

11
10 - 2번, 0 1개 제거

1
1 - 3번, 0 1개 제거

[3, 8] - return 값

'''
