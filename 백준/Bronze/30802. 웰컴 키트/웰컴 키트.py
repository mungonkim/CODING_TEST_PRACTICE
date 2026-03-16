import sys
input = sys.stdin.readline

N = int(input())
s_list = list(map(int, input().split()))
T, P = map(int, input().split())

result = 0
for i in s_list:
    result += (i+T-1) // T
    
print(result)
print(N//P, N%P)