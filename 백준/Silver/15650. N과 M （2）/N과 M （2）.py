import sys
sys.stdin.readline

N, M = map(int, input().split())
result = []

def dfs(start, depth):
    if depth == M:
        print(*result)
        return 
    
    for i in range(start, N+1):
        result.append(i)
        dfs(i+1, depth+1)
        result.pop()
  
dfs(1, 0)