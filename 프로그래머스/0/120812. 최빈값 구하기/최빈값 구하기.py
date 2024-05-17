def solution(array):
    list = [0] * (max(array)+1)
    for i in array:
        list[i] += 1
    result = 0
    for j in list:
        if j == max(list):
            result += 1
    if result > 1:
        return -1
    else:
        return list.index(max(list))