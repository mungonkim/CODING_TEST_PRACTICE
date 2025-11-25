def solution(arr):
    n = len(arr)
    power = 1
    while power < n:
        power *= 2
    
    arr += [0] * (power - n)
    return arr
