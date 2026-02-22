import sys
input = sys.stdin.readline

color_value = {
    "black": (0, 1),
    "brown": (1, 10),
    "red": (2, 100),
    "orange": (3, 1000),
    "yellow": (4, 10000),
    "green": (5, 100000),
    "blue": (6, 1000000),
    "violet": (7, 10000000),
    "grey": (8, 100000000),
    "white": (9, 1000000000)
}

a = input().strip()
b = input().strip()
c = input().strip()

first = color_value[a][0]
second = color_value[b][0]
mul = color_value[c][1]

result = int(str(first) + str(second)) * mul
print(result)