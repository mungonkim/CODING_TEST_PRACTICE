def solution(picture, k):
    answer = []
    for i in picture:
        str = ''
        for j in range(len(i)):
            str += i[j]*k
        answer+= [str]*k
    return answer