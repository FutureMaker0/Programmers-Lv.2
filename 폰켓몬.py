def solution(nums):
    return min(len(set(nums)), len(nums)/2)
    
    
'''
{1, 2, 3}
{2, 3, 4}
{2, 3}


3 3 3 2 2 4 4 1
{1 2 3 4} - 4
[] - 4
'''
