import sys
input = sys.stdin.readline

vowel = ['a', 'i', 'e', 'o', 'u']
result = 0

n = int(input())
ch = input()
for i in ch:
    if i in vowel:
        result += 1

print(result)