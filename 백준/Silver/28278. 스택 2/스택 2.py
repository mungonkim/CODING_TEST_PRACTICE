import sys

input = sys.stdin.readline

n = int(input())
result = []

for _ in range(n):
    answer = input().split()
    cnt = int(answer[0])
    
    if cnt == 1:
        result.append(int(answer[1]))
    elif cnt == 2:
        if result:
            print(result.pop())
        else:
            print(-1)
    elif cnt == 3:
        print(len(result))
    elif cnt == 4:  # 
        if result:
            print(0)
        else:
            print(1)
    elif cnt == 5:
        if result:
            print(result[-1])
        else:
            print(-1)
