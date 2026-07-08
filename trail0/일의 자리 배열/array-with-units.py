n1, n2 = map(int, input().split())

arr = [n1, n2]

for i in range(8):
    arr.append((arr[-2]+arr[-1])%10)

print(*arr)