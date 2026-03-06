code = input()
N = int(input())

result = 0

for _ in range(N):
    r_code = input()
    if code[:5] == r_code[:5]:
        result += 1

print(result)
