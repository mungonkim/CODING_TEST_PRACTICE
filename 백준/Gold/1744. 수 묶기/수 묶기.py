n = int(input())
num = []

plus = []
minus = []
result = 0

for _ in range(n):
    num = int(input())
    if num > 1:
        plus.append(num)
    elif num <= 0:
        minus.append(num)
    else:
        result += num
        
plus.sort(reverse=True)
minus.sort()

if len(plus) % 2 == 1:
    result += plus[len(plus) -1]
    for j in range(0, len(plus)-1, 2):
        result += plus[j] * plus[j+1]

else:
    for j in range(0, len(plus), 2):
        result += plus[j] * plus[j+1]

if len(minus) % 2 == 1:
    result += minus[len(minus) -1]
    for j in range(0, len(minus)-1, 2):
        result += minus[j] * minus[j+1]

else:
    for j in range(0, len(minus), 2):
        result += minus[j] * minus[j+1]
        
print(result)