import sys

input = sys.stdin.readline

x = input().rstrip()
count = 0


while len(x) > 1:
    y = 0
    for i in range(len(x)):
        y += int(x[i])
    count += 1
    x = str(y)

if int(x) % 3 == 0:
    print(count)
    print('YES')
else:
    print(count)
    print('NO')