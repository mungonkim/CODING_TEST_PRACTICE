import sys

n = int(input())

dot = []
length = 0

for _ in range(n):
    dot.append(tuple(map(int, input().split())))

dot.sort()    

max_dot = -sys.maxsize

for start, end in dot:
    if start >= max_dot:
        length += (end - start)
    else:
        if end > max_dot:
            length += (end - max_dot)
    
    max_dot = max(end, max_dot)
    
print(length)