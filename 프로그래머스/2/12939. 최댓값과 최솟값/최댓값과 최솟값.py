'''
def solution(s):
    answer = ''
    s_list = s.split(' ')

    answer = min(s_list, key=int)+ ' ' + max(s_list, key=int)
    return answer
'''

def solution(s):
    nums = list(map(int, s.split()))
    
    return f"{min(nums)} {max(nums)}"