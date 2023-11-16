N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

result = 0

A.sort()
B.sort(reverse = True)

for i in range(N):
    s = A[i] * B [i]
    
    result += s

print(result)
