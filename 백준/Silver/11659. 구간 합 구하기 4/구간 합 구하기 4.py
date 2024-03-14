import sys

input = sys.stdin.readline

N, M = map(int, input().split())

nums = list(map(int, input().split()))

sums = [0]
temp = 0

for i in range(N):
    temp += nums[i]
    sums.append(temp)

for _ in range(M):
    i, j = map(int, input().split())
    print(sums[j] - sums[i-1])