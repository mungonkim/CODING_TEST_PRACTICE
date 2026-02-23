s, d = map(int, input().split())

if (s+d) % 2 or (s-d) % 2 or s < d:
    print(-1)
else:
    x = (s+d)//2
    y = (s-d)//2
    print(x, y)