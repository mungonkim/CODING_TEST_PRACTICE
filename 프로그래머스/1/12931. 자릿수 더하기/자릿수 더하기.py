def solution(n):
    answer = 0
    
    result = list(str(n))
    
    for i in result:
        answer += int(i)

    return answer