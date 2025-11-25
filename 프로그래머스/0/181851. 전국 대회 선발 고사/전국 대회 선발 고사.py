def solution(rank, attendance):
    result = []
    for i in range(len(rank)):
        student = rank.index(i+1)   
        if attendance[student]:
            result.append(student)
        if len(result) == 3:
            break

    return 10000 * result[0] + 100 * result[1] + result[2]
