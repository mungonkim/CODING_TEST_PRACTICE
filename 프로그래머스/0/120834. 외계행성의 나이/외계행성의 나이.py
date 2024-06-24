def solution(age):
    
    age = str(age)
    answer = ''
    for i in range(len(age)):
        answer += chr(ord("a") + int(age[i]))
    
    return answer