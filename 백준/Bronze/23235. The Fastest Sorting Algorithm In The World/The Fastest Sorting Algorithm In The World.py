import sys
input = sys.stdin.readline
cnt = 1
while True:
    n_list = list(map(int, input().split()))
    if n_list[0] == 0:
        break
    print(f'Case {cnt}: Sorting... done!')
    cnt += 1
    