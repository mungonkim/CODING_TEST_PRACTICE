while True:
    line = list(map(int, input().split()))

    if line[0] == 0 and line[1] == 0 and line[2] == 0:
        break
    elif max(line) >= sum(line) - max(line):
        print('Invalid')
    elif line[0] == line[1] == line[2]:
        print('Equilateral')
    elif (line[0] == line[1] != line[2]) or (line[1] == line[2] != line[0]) or (line[0] == line[2] != line[1]) :
        print('Isosceles')
    else:
        print('Scalene')