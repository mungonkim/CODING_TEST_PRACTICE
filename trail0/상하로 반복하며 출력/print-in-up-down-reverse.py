n = int(input())

arr = [[0 for i in range(n)] for i in range(n)]

for i in range(n):
    if (i+1) % 2 != 0:
        for j in range(1, n+1):
            arr[j-1][i] = j
    else:
        for j in range(n, 0, -1):
            arr[n-j][i] = j

for i in range(n):
    for j in range(n):
        print(arr[i][j], end='')
    print()