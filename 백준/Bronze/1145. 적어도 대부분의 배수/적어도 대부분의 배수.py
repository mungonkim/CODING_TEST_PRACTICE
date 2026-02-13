n = list(map(int, input().split()))

result = 1

while True:
    cnt = 0
    for i in n:
        if result % i == 0:
            cnt += 1
    if cnt >= 3:
        print(result)
        break
    
    result += 1
