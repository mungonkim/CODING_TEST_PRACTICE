import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n = input().strip()
    reverse_n = n[::-1]
    
    result = str(int(n) + int(reverse_n))
    
    if result == result[::-1]:
        print('YES')
    else:
        print('NO')
            