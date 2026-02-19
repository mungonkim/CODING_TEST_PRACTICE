L, P = map(int, input().split())

people = list(map(int, input().split()))

for i in range(5):
    print(people[i] - L*P, end=' ')