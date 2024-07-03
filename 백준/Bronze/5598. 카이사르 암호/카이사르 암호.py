import sys

input = sys.stdin.readline

word = input().rstrip()
result = ''

for i in word:
    if ord(i) < ord('D'):
        result += chr(ord(i) + 23)
    else:
        result += chr(ord(i) - 3)

print(result)   