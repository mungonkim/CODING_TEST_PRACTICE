n = int(input())

for i in range(n):
    if (i+1) % 2 != 0:
        for i in range(1, n+1):
            print(i, end='')
    else:
        for i in range(n, 0, -1):
            print(i, end='')
    print()