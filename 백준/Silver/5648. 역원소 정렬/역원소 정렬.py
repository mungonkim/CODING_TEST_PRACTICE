import sys
input = sys.stdin.read

n, *nums = input().split()

result = []
for i in range(int(n)):
    word = nums[i]
    word = "".join(reversed(word))
    word = int(word)
    result.append(word)

result.sort()

for i in result:
    print(i)