def solution(babbling):
    list = ['aya', 'ye', 'woo', 'ma']
    answer = 0
    for i in babbling:
        temp = i
        for j in list:
            temp = temp.replace(j, '*')
        if temp.replace('*', '') == '':
            answer += 1
    return answer