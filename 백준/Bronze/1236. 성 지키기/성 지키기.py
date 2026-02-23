import sys
input = sys.stdin.readline

N, M = map(int, input().split())
castle = []
result1 = 0
result2 = 0

for _ in range(N):
    ch = input().strip()
    castle.append(ch)

for i in range(M):
    flag = 0
    for j in range(N):
        if castle[j][i] == 'X':
            flag = 1
    if flag == 0:
        result1 += 1

for i in castle:
    if 'X' not in i:
        result2 += 1
    
print(max(result1, result2))