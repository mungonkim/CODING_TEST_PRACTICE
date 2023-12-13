import sys

input = sys.stdin.readline

t = int(input())
floor =[]

for _ in range(t):
    a = int(input())
    b = int(input())
    
    dp = [0] * (b+1)
    for i in range(b+1):
        dp[i] = i 
    
    for i in range(1, a+1):
        for j in range(1, b+1):
            if j == 1:
                dp[j] = 1
            dp[j] = dp[j] + dp[j-1]

    print(dp[b])