def solution(numbers):
    n = len(numbers)
    answer = 0
    for i in numbers:
        answer += i
    return answer/n