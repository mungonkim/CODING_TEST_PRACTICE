n = int(input())
count = 0

while n >= 5:
    n //= 5
    count += n

print(count)





# 처음에 짠 코드는 런타임 에러 발생(n이 커지면 커질수록 재귀 깊이 한계를 넘음)
'''def fac(n):
    if n == 1:
        return 1
    return n * fac(n-1)

n = int(input())
cnt = 0

num = fac(n)
result = list(str(num))

for i in reversed(result):
    if i == '0':
        cnt += 1
    else:
        break
print(cnt)
'''