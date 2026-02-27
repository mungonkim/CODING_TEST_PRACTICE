import sys
import math
input = sys.stdin.readline

LIMIT = 10**6
N = int(input())

for _ in range(N):
    S = int(input())
    ok = True

    max_check = min(LIMIT, int(math.isqrt(S)))

    for i in range(2, max_check + 1):
        if S % i == 0:
            ok = False
            break

    print("YES" if ok else "NO")