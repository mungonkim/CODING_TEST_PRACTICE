n = int(input())
person = []

for _ in range(n):
    name, dd, mm, yyyy = input().split()
    person.append((name, int(dd), int(mm), int(yyyy)))

person.sort(key = lambda person: (person[3], person[2], person[1]))

print(person[-1][0])
print(person[0][0])