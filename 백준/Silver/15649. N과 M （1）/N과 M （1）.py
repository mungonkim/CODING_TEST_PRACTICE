import sys
input = sys.stdin.readline

N, M = map(int, input().split())
visited = [False] * (N + 1)
result = []

def dfs(depth):
    if depth == M:
        print(*result)
        return
    
    for i in range(1, N + 1):
        if not visited[i]:
            visited[i] = True
            result.append(i)
            dfs(depth + 1)
            result.pop()
            visited[i] = False

dfs(0)
