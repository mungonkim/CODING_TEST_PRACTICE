def solution(balls, share):
    answer = 0
    
    answer = fact(balls) / (fact(balls-share) * fact(share)) 
    return int(answer)

def fact(num):
    result = 1
    for i in range(1, num +1):
        result *= i
    return result