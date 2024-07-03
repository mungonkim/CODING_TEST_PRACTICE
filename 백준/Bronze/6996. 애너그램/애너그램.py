import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    a,b = input().split()

    if sorted(a) == sorted(b):
        print(a + ' & ' + b + ' are anagrams.')
    else:
        print(a + ' & ' + b + ' are NOT anagrams.')