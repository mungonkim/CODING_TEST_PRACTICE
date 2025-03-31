def solution(order):
    answer = 0
    order = str(order)

    for i in order:
        if i in '3' or i in '6' or i in '9':
            answer += 1

    return answer
