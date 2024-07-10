def fact(num):
    result = 1
    for i in range(1, num+1):
        result *= i
    return result

def solution(n):
    answer = 1
    result = 0
    while result <= n:
        answer += 1
        result = fact(answer)
    return answer - 1