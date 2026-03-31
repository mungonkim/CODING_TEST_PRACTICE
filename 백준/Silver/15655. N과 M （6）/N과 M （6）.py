import sys

input = sys.stdin.readline

N, M = map(int, input().split())
n_list = list(map(int, input().split()))
n_list.sort()
result = []

def dfs(start, depth):
    if depth == M:
        print(*result)
        return 
    
    for i in range(start, N):
        result.append(n_list[i])
        dfs(i+1, depth+1)
        result.pop()

dfs(0, 0)