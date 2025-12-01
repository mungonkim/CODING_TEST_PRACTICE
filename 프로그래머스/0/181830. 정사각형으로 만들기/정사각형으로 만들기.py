def solution(arr):
    n = len(arr) # 행의 수
    m = len(arr[0]) # 열의 수
    if m > n:
        for _ in range(m-n):
            arr.append([0]*m)
    else:
        for i in range(n):
            arr[i] += [0]*(n-m)
        
    return arr