def solution(intStrs, k, s, l):
    answer = []
    for t in intStrs:                   
        num = int(t[s:s + l])           
        if num > k:
            answer.append(num)         
    return answer
