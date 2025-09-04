def solution(n):
    answer = []
    for i in range(n):
        list = []
        for j in range(n):
            if i == j:
                list.append(1)
            else:
                list.append(0)
        answer.append(list)
    return answer