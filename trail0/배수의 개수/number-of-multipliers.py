t_cnt = 0
f_cnt = 0

for _ in range(10):
    num = int(input())
    if num % 3 == 0:
        t_cnt += 1

    if num % 5 == 0:
        f_cnt += 1

print(t_cnt, f_cnt)