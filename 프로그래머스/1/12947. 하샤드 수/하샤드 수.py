def solution(x):
    result = sum(int(i) for i in str(x))
    
    return x % result == 0