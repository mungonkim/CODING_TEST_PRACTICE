import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    M, N, x, y = map(int, input().split())
    
    year = x
    answer = -1
    
    while year <= M * N:
        if (year - y) % N == 0:
            answer = year
            break
        year += M

    print(answer)
 
#기존 코드 but 시간 초과
'''
import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    m, n, x, y = map(int, input().split())
    cnt1, cnt2 = 1, 1
    result = 1
    flag = False
    
    for _ in range(M*N+1):
        if cnt1 == x and cnt2 == y:
            flag = True
            break
        
        cnt1 += 1
        cnt2 += 1
        
        if cnt1 > m:
            cnt1 = 1
        if cnt2 > n:
            cnt2 = 1
            
        result += 1
    
    if flag == True:
        print(result)
    else:
        print(-1)
 '''