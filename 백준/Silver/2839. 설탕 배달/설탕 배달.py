N = int(input())

kgs = [3, 5]
sugars = [0] + [N+1]*N

for kg in kgs:
    for i in range(kg, N+1):
        sugars[i] = min(sugars[i], sugars[i-kg]+1)

if sugars[N] >= N+1:
    print(-1)
else:
    print(sugars[N])