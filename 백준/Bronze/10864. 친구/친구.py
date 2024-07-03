import sys

n,m = map(int, sys.stdin.readline().split())

result = [0] * (n+1)

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    result[a] += 1
    result[b] += 1

for i in range(1, n+1):
    print(result[i])