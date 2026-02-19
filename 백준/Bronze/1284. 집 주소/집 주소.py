while True:
    n = input()
    if n == '0':
        break

    width = 2  # 양쪽 여백

    for ch in n:
        if ch == '1':
            width += 2
        elif ch == '0':
            width += 4
        else:
            width += 3

    width += len(n) - 1  # 숫자 사이 여백

    print(width)

# 처음 접근 방식
'''while True:
    sum = 0
    n = input()
    if n == '0':
        break
    
    for i in range(len(n)):
        if i == 0:
            if n[i] == '1':
                sum += 2*2
            elif n[i] == '0':
                sum += 4*2
            else:
                sum += 3*2
        else:
            if n[i] == '1':
                sum += 2
            elif n[i] == '0':
                sum += 4
            else:
                sum += 3
    print(sum + 2)
'''
