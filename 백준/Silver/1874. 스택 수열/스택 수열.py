T = int(input())
i = 1
stack = []
result = []
flag = 1
for _ in range(T):
    n = int(input())

    while i <= n:
        stack.append(i)
        result.append('+')
        i += 1

    if stack.pop() != n:
        flag = 0
        break
    else:
        result.append('-')

if flag == 0:
    print("NO")
else:
    for i in result:
        print(i)