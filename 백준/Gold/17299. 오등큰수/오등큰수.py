'''
# 원래 코드 출력 결과 시간초과 발생
import sys

input = sys.stdin.readline

n = int(input())

n_list = list(map(int, input().split()))

for i in range(len(n_list)):
    flag = 0
    for j in range(i + 1, len(n_list)):
        if n_list.count(n_list[i]) < n_list.count(n_list[j]):
            print(n_list[j], end=" ")
            flag = 1
            break
    if flag == 0:
        print('-1', end=" ")
'''
# 시간 초과 해결 코드
import sys 

input = sys.stdin.readline

N = int(input())
n_list = list(map(int, input().split()))

count = [0] * 1000001
stack = []
res = [-1] * N

for n in n_list:
    count[n] += 1

for i in range(N):
    while stack and count[n_list[stack[-1]]] < count[n_list[i]]:
        res[stack.pop()] = n_list[i]
    stack.append(i)

print(*res)