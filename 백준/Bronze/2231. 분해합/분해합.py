N = int(input())

for i in range(N):
    if i + sum(map(int, str(i))) == N:
        print(i)
        break
else:
    print(0)