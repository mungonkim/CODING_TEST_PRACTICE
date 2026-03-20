N, A, B = map(int, input().split())

if N + A < N+B:
    print('Bus')
elif N + A > N+B:
    print('Subway')
else:
    print('Anything')