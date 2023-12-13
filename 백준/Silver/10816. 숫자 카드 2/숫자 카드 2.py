import sys
input = sys.stdin.readline

n = int(input())
nums_a = list(map(int, input().split()))

m = int(input())
nums_b = list(map(int, input().split()))

d = {}

for i in nums_a:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

for i in nums_b:
    if i in d:
        print(d[i], end=" ")
    else:
        print(0, end=" ")