import sys
input = sys.stdin.readline

N,M = map(int, input().split())
n_list = list(map(int, input().split()))
result = []
n_list.sort()

def dfs(depth):
    if depth == M:
        print(*result)
        return 
    
    for i in n_list:
        result.append(i)
        dfs(depth+1)
        result.pop()

dfs(0)