n = int(input())

people = []
result = []

for _ in range(n):
    cm, kg = map(int, input().split())
    people.append([cm, kg])

for i in range(n):
    rank = 1
    for j in range(n):
        if people[i][0] < people[j][0] and people[i][1] < people[j][1]:
            rank += 1
    result.append(rank)

print(*result)
    