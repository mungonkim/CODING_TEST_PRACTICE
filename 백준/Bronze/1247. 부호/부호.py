for _ in range(3):
    n = int(input())
    sum = 0
    for _ in range(n):
        s = int(input())
        sum += s
    if sum > 0:
        print('+')
    elif sum == 0:
        print(0)
    else:
        print('-')
