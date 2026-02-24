import sys
input = sys.stdin.readline

e, s, m = map(int, input().split())

n1, n2, n3 = 1, 1, 1
result =1
while True:
    if n1 == e and n2 == s and n3 == m:
        break
    n1 += 1
    n2 += 1
    n3 += 1
    
    if n1 > 15:
        n1 = 1
    if n2 > 28:
        n2 = 1
    if n3 > 19:
        n3 = 1
    
    result += 1

print(result)