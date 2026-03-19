import sys
input = sys.stdin.readline

ch = input().rstrip()

for i in range(10):
    result = 0
    temp = list(ch)  

    for j in range(len(temp)):
        if temp[j] == '*':
            temp[j] = str(i)

        if (j+1) % 2 == 1:  # 홀수 자리
            result += int(temp[j])
        else:               # 짝수 자리
            result += int(temp[j]) * 3

    if result % 10 == 0:
        print(i)
        break