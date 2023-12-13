import sys

input = sys.stdin.readline

n = int(input())
num_a = list(map(int, input().split()))

m = int(input())
num_b = list(map(int, input().split()))

d = { }

for i in num_a:
    if i not in d:
        d[i] = 1
    else:
        d[i] += 1

for i in num_b:
    if i in d:
        print(d[i], end=" ")
    else:
        print(0, end=" ")