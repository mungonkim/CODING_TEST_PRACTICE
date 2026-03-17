n, k = map(int, input().split())

k = min(k, n - k)  # 대칭성 활용

result = 1
for i in range(k):
    result *= (n - i)
    result //= (i + 1)

print(result)