def solution(arr):
    for idx in range(len(arr)):
        if arr[idx] >= 50 and arr[idx] % 2 == 0:  
            arr[idx] //= 2
        elif arr[idx] < 50 and arr[idx] % 2 == 1: 
            arr[idx] *= 2
    return arr
