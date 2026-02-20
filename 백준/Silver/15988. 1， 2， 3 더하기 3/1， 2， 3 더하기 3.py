T = int(input())

dp = [0]*1000001

for i in range(1, 1000001):
    if i == 1:
        dp[i] = 1
    elif i == 2:
        dp[2] = 2
    elif i == 3:
        dp[3] = 4
    else:
        dp[i] = (dp[i-3] + dp[i-2] + dp[i-1]) % 1000000009
        
for _ in range(T):
    n = int(input())
    print(dp[n])