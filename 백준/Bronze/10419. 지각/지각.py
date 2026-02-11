n = int(input())

for _ in range(n):
    time = 0
    s_time = int(input())
    
    while (time+1) + (time+1)**2 <= s_time:
        time += 1
        
    print(time) 