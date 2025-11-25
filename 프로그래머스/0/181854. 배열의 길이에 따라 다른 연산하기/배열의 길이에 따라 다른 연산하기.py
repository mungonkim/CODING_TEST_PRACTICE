def solution(arr, n):
    target = 0 if len(arr) % 2 else 1  
    for i in range(target, len(arr), 2):
        arr[i] += n
    return arr
