n = int(input())
chosen = []

for _ in range(n):
    line = input().split()
    d = int(line[0])
    dishes = line[1:]
    chosen = dishes

print(len(chosen))
for dish in chosen:
    print(dish)
