n_list = list(map(int, input().split()))

result = 0
for i in range(1, len(n_list)):
    if n_list[0] - n_list[i] <= 1000:
        result += 1

print(result)