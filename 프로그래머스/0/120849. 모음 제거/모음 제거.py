def solution(my_string):
    answer = ''
    alpht = ['a', 'e', 'i', 'o', 'u']

    for i in my_string:
        if i not in alpht:
            answer+=i

    return answer