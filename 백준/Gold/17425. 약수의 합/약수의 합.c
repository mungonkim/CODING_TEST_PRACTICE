#include <stdio.h>

#define MAX 1000000

long long f[MAX + 1];  // f(n) = n의 약수 합
long long g[MAX + 1];  // g(n) = 1~n까지 f(y)의 누적 합

int main() {
    // f(n) 채우기: 모든 i의 배수 j에 i를 더함 (에라토스 방식)
    for (int i = 1; i <= MAX; i++) {
        for (int j = i; j <= MAX; j += i) {
            f[j] += i;
        }
    }

    // g(n): 누적 합
    g[1] = f[1];
    for (int i = 2; i <= MAX; i++) {
        g[i] = g[i - 1] + f[i];
    }

    int T, n;
    scanf("%d", &T);
    while (T--) {
        scanf("%d", &n);
        printf("%lld\n", g[n]);
    }

    return 0;
}
