a, b, c = map(int, input().split())

if a == b == c:
    print(a * 3)
elif sum((a, b, c)) - max(a, b, c) > max(a, b, c):
    print(a + b + c)
else:
    print((sum((a, b, c)) - max(a, b, c) - 1) + (sum((a, b, c)) - max(a, b, c)))
