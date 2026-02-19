N, M = map(int, input().split())

for _ in range(N):
    ch = input()
    if ch.count('O') <= M // 2:
        N -= 1

print(N)
