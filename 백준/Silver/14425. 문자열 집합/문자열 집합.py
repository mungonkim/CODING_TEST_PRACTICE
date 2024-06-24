n, m = map(int, input().split())

words = set()
count = 0

for _ in range(n):
    word = input()
    words.add(word)

for _ in range(m):
    find = input()
    if find in words:
        count += 1

print(count)