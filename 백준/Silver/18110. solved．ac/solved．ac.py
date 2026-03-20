import sys

input = sys.stdin.readline

n = int(input())

if n == 0:
    print(0)
    exit()

arr = [int(input()) for _ in range(n)]
arr.sort()

cut = int(n * 0.15 + 0.5)

trimmed = arr[cut:n-cut]

avg = sum(trimmed) / len(trimmed)

print(int(avg + 0.5))