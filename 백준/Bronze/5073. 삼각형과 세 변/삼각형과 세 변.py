while True:
    A, B, C = list(map(int, input().split()))

    if A == 0 and B == 0 and C == 0:
        break
    elif max((A, B, C)) >= sum((A, B, C)) - max((A, B, C)):
        print('Invalid')
    elif A == B == C:
        print('Equilateral')
    elif (A == B != C) or (B == C != A) or (A == C != B) :
        print('Isosceles')
    else:
        print('Scalene')
    