def solution(arr, queries):
    answer = []
    for s, e, k in queries:
        result = float('inf')
        for i in range(s, e+1):
            if arr[i] > k and arr[i] < result:
                result = arr[i]
        answer.append(-1 if result == float('inf') else result)
            
    return answer