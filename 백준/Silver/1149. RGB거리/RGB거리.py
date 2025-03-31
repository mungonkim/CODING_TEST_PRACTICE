n = int(input())

color = [list(map(int, input().split())) for _ in range(n)]

for i in range(1, n):
    # 빨강을 선택할 경우: 이전 집의 초록 or 파랑 중 최소
    color[i][0] += min(color[i-1][1], color[i-1][2])
    # 초록을 선택할 경우: 이전 집의 빨강 or 파랑 중 최소
    color[i][1] += min(color[i-1][0], color[i-1][2])
    # 파랑을 선택할 경우: 이전 집의 빨강 or 초록 중 최소
    color[i][2] += min(color[i-1][0], color[i-1][1])

print(min(color[n-1]))