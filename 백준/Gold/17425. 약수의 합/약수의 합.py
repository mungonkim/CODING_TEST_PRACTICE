import sys

input = sys.stdin.readline

MAX = 1000000

f = [0] * (MAX + 1) # f(n) 1 ~ n 까지의 약수 합

g = [0] * (MAX + 1) # g(n)은 1 ~ n까지 f(y)의 누적 합

for i in range(1, MAX+1):
    for j in range(i, MAX+1, i):
        f[j] += i

for i in range(1, MAX+1):
    g[i] = g[i-1] + f[i]
    

T = int(input())
for _ in range(T):
    n = int(input())
    print(g[n])
