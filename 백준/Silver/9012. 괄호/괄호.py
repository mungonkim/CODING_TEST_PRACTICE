n = int(input())

for _ in range(n):
    word = input()
    stack = []
    for i in word:
        if i == "(":
            stack.append(i)
        elif i == ")":
            if stack:
                stack.pop()
            else:
                stack.append(i)
                break
    if stack:
        print("NO")
    else:
        print("YES")