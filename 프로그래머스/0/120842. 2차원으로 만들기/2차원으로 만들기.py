def solution(num_list, n):
    answer = []

    for i in range(len(num_list) // n):
        list = []
        for j in range(n):
            list.append(num_list.pop(0))
        answer.append(list)
    return answer