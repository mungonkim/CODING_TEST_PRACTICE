import sys

input = sys.stdin.readline

n, l = map(int, input().split())

num = list(map(int, input().split()))
num.sort()

for i in num:
    if l >= i:
        l += 1

print(l)