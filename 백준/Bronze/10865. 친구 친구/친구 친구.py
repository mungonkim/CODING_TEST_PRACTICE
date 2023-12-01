import sys
input = sys.stdin.readline

N, M = map(int, input().split())

result = [0] * (N + 1)

for i in range(M):
    A, B = map(int, input().split())
    result[A] += 1
    result[B] += 1


for i in range(1, N+1):
    print(result[i])