def solution(myString):
    result = []
    cnt = 0
    for i in range(len(myString)):
        if myString[i] == 'x':
            result.append(cnt)
            cnt = 0
        else:
            cnt+=1
    result.append(cnt)
    return result