def solution(a, d, included):
    answer = 0
    result = a
    for i in range(len(included)):
        if included[i] == True:
            answer += result
        result += d
            
    return answer