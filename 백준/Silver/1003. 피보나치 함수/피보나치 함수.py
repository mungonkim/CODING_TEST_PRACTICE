import sys

input = sys.stdin.readline

n = int(input())
dzero = [0] * (n+1)
done = [0] * (n+1)

for _ in range(n):
    v = int(input())

    dzero = [0] * (v+1)
    done = [0] * (v+1)

    for i in range(0, v+1):
        if i == 0:
            dzero[i] = 1
            done[i] = 0
        elif i == 1:
            dzero[i] = 0
            done[i] = 1
        else:
            dzero[i] = dzero[i-1] + dzero[i-2]
            done[i] = done[i-1] + done[i-2]
    print(dzero[v], done[v])
        