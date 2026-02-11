n = int(input())

n_list = list(map(int, input().split()))
n_list.sort()
total = 0

pre_sum = [0] * (n+1)

for i in range(n):
    pre_sum[i+1] = pre_sum[i] + n_list[i]
    
for i in range(n):
    left = n_list[i] * i - pre_sum[i]
    
    right = (pre_sum[n] - pre_sum[i+1]) - n_list[i] * (n-i-1)
    
    total += left + right

print(total)