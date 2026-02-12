word = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

while True:
    count = 0
    s = input()
    if s == '#':
        break
    for ch in s:
        if ch in word:
            count += 1
    print(count)
    