def solution(a, b, c):
    
    if a == b == c:
        return (a+b+c)*(pow(a,2)+pow(b,2)+pow(b,2))*(pow(a,3)+pow(b,3)+pow(c,3))
    elif a != b and b != c and a != c:
        return a+b+c
    else:
        return (a+b+c) * (pow(a,2)+pow(b,2)+pow(c,2))