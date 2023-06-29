def solution(s):
    answer = ''
    
    num_list = s.split(' ')
    num_list = [int(num) for num in num_list]
    
    return f'{min(num_list)}' + ' ' + f'{max(num_list)}'



'''
채점 결과
정확성: 100.0
합계: 100.0 / 100.0
'''
