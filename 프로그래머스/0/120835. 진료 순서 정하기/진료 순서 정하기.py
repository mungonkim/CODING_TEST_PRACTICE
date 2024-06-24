def solution(emergency):
    n = len(emergency)
    answer = [1] * n

    for i in range(n):
        for j in range(n):
            if emergency[i] < emergency[j]:
                answer[i] += 1
    return answer