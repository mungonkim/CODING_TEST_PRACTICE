import sys

input = sys.stdin.readline

list1 = []

for _ in range(5):
    s = input().strip()
    list1.append(list(s))

for i in range(15):
    for j in range(5):
        if i < len(list1[j]):
            print(list1[j][i], end='')
        