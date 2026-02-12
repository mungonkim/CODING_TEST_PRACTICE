cycle = {
    0: [10],
    1: [1],
    2: [2,4,8,6],
    3: [3,9,7,1],
    4: [4,6],
    5: [5],
    6: [6],
    7: [7,9,3,1],
    8: [8,4,2,6],
    9: [9,1]
}

t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    a %= 10
    result = cycle[a][(b - 1) % len(cycle[a])]
    print(result)

# 처음 작성한 코드(시간 초과 발생)    
'''
n = int(input())

for _ in range(n):
    a, b = map(int, input().split())
    total = pow(a, b)
    while len(str(total)) != 1:
        total %= 10
    if total  == 0:
        print(10)
    else:
        print(total)    
'''
