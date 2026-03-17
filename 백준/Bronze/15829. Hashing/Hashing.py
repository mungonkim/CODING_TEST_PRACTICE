import sys
input = sys.stdin.readline

n = int(input())
ch = input().strip()

M = 1234567891
result = 0

for i in range(len(ch)):
    result += (ord(ch[i]) - 96) * pow(31, i, M)
    result %= M

print(result)