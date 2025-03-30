def solution(array, n):
    answer = array[0]
    cnt = abs(array[0] - n)

    for i in range(1, len(array)):
        if abs(array[i] - n) < cnt:
            cnt = abs(array[i] - n)
            answer = array[i]
        elif abs(array[i] - n) == cnt:
            answer = min(answer, array[i])
    return answer
