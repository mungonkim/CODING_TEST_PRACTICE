import sys

words = sys.stdin.readline().strip()
stack = []
result = ''
check = False

for w in words:
    if w == '<':
        check = True
        for _ in range(len(stack)):
            result += stack.pop()
    stack.append(w)
    
    if w == '>':
        check = False    
        for _ in range(len(stack)):
            result += stack.pop(0)

    if w == " " and check == False:
        for i in range(len(stack)):
            if i == 0:
                stack.pop()
                continue
            result += stack.pop()
        result += " "

if stack:
    for _ in range(len(stack)):
        result += stack.pop()

print(result)