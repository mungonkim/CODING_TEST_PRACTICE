height, N = map(int, input().split())

for _ in range(N):
    if height % 2 == 0:
        height = (height // 2) ^ 6
    elif height % 2 == 1:
        height = (height * 2) ^ 6

print(height)