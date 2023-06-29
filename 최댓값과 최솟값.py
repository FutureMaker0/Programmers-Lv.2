def solution(s):
    answer = ''
    
    num_list = s.split(' ')
    num_list = [int(num) for num in num_list]
    
    return f'{min(num_list)}' + ' ' + f'{max(num_list)}'

