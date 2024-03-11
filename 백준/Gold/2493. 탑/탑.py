import sys

input = sys.stdin.readline

n = int(input())

high = list(map(int, input().split()))

result = [0] * n
stack = []

for i in range(n):
    while stack:
        if stack[-1][1] > high[i]:
            result[i] = stack[-1][0] + 1
            break
        else:
            stack.pop()

    stack.append([i, high[i]])

print(*result)