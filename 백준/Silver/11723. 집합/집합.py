import sys
input = sys.stdin.readline

num = int(input())
s = set()

for _ in range(num):
    temp = input().strip().split()

    if temp[0] == 'add':
        s.add(int(temp[1]))

    elif temp[0] == 'remove':
        s.discard(int(temp[1]))

    elif temp[0] == 'check':
        print(1 if int(temp[1]) in s else 0)

    elif temp[0] == 'toggle':
        x = int(temp[1])
        if x in s:
            s.remove(x)
        else:
            s.add(x)

    elif temp[0] == 'all':
        s = set(range(1, 21))

    elif temp[0] == 'empty':
        s.clear()