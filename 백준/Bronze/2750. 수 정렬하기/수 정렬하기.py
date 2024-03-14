import sys

input = sys.stdin.readline

n = int(input())
nums = []
for i in range(n):
    nums.append(int(input()))

for i in range(n-1):
    for j in range(i+1, n):
        if(nums[i] > nums[j]):
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp

for i in range(n):
    print(nums[i])