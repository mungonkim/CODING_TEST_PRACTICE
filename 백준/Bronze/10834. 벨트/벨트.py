import sys
input = sys.stdin.readline

m = int(input())
dir = 0
result = 1

for _ in range(m):
    a, b, flag = map(int, input().split())
    if flag == 1:
        if dir == 0:
            dir = 1
        else:
            dir = 0
            
    result = result * b / a
    
print(dir, int(result))