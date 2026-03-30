import sys
input = sys.stdin.readline

N,M = map(int, input().split())
n_list = list(map(int, input().split()))
n_list.sort()
visited = [False] * (N+1)
result = []

def dfs(depth):
    if depth == M:
        print(*result)
        return 
    
    for i in n_list:
        if i in result:
            continue
        result.append(i)
        dfs(depth+1)
        result.pop()

dfs(0)