import sys
input = sys.stdin.readline

t1, n1 = map(int, input().split())
t2, n2 = map(int, input().split())
t3, n3 = map(int, input().split())

for i in range(1, 101):
    if i % 3 == 1:
        if n1 + n2 > t2:
            n1 = n1 + n2 - t2
            n2 = t2
        else:
            n2 = n1 + n2
            n1 = 0
    elif i % 3 == 2:
        if n2 + n3 > t3:
            n2 = n2 + n3 - t3
            n3 = t3
        else:
            n3 = n2 + n3
            n2 = 0
    elif i % 3 == 0:
        if n1 + n3 > t1:
            n3 = n1+n3 - t1
            n1 = t1
        else:
            n1 = n1 + n3
            n3 = 0

print(n1)
print(n2)
print(n3)
