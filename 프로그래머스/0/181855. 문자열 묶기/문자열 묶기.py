def solution(strArr):
    result = [0] * (len(strArr)+1)
    for i in strArr:
        result[len(i)] += 1
        
    return max(result)