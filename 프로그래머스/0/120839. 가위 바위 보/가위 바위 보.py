def solution(rsp):
    menu = {'2':'0', '0':'5', '5': '2'}
    answer = ''
    for i in rsp:
        answer += menu[i]
    return answer
