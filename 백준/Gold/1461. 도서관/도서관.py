n , m = map(int, input().split())
book = list(map(int, input().split()))

plus = []
minus = []

distance = 0
result = 0
max = 0

for i in book:
    if abs(i) > max:
        max = abs(i)
    if i > 0:
        plus.append(i)
    else:
        minus.append(i)

plus.sort(reverse = True)
minus.sort()

for i in range(0, len(plus), m):
    if plus[i] != max:
        distance += plus[i]
        
for i in range(0, len(minus), m):
    if abs(minus[i]) != max:
        distance += abs(minus[i])

result = distance*2 + max

print(result)